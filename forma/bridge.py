import json
import sys
from typing import Any, Dict, List, Optional

from forma.templates import TEMPLATES
from forma.engine import generate_from_template


def _get_subcategories_mapping(template: Dict[str, Any]) -> Dict[str, Any]:
  """
  Some templates use 'subcategories', others use 'Subcategories'.
  Normalise this so the rest of the API can be casing-agnostic.
  """
  return template.get("subcategories") or template.get("Subcategories") or {}


def get_templates_metadata() -> List[Dict[str, Any]]:
  """
  Lightweight metadata for all templates and their subcategories.
  Intended for programmatic / web usage (no heavy objects, just names).
  """
  meta: List[Dict[str, Any]] = []
  for template_name, template in TEMPLATES.items():
    sub_map = _get_subcategories_mapping(template)
    subcategories = list(sub_map.keys())
    meta.append(
      {
        "id": template_name,
        "name": template_name,
        "subcategories": subcategories,
      }
    )
  return meta


def generate_data(
  template_id: str,
  selected_subcategories: List[str],
  count: int,
  seed: Optional[int] = None,
) -> List[Dict[str, Any]]:
  """
  Generate synthetic rows for a given template and subcategories.
  Returns a list of plain Python dicts (JSON serialisable).
  """
  if template_id not in TEMPLATES:
    raise ValueError(f"Unknown template id: {template_id}")

  raw_template = TEMPLATES[template_id]
  sub_map = _get_subcategories_mapping(raw_template)

  # Build a normalised template object for the generator
  template: Dict[str, Any] = dict(raw_template)
  template["subcategories"] = sub_map

  df = generate_from_template(template, selected_subcategories, count, seed)
  return df.to_dict(orient="records")


def handle(payload: Dict[str, Any]) -> Dict[str, Any]:
  """
  Run one request from the Node.js server in server/.

  Expected payload:
      {"action": "list_templates"}
  or:
      {
        "action": "generate",
        "templateId": "<template name>",
        "subcategories": ["User Info", "Device Info"],
        "count": 100,
        "seed": 42   # optional
      }

  Errors come back as {"error": "..."} so callers can surface them nicely.
  """
  try:
    action = payload.get("action")

    if action == "list_templates":
      return {"templates": get_templates_metadata()}

    if action == "generate":
      template_id = payload["templateId"]
      subcats = payload.get("subcategories") or []
      count = int(payload.get("count", 1))
      seed = payload.get("seed")
      if seed is not None:
        seed = int(seed)

      return {"rows": generate_data(template_id, subcats, count, seed)}

    raise ValueError(f"Unknown action: {action}")
  except Exception as exc:  # noqa: BLE001
    return {"error": str(exc)}


def app(environ, start_response):
  """
  WSGI entry point, used when the server reaches Python over HTTP
  (on Vercel the Python code runs as its own service).
  """
  try:
    size = int(environ.get("CONTENT_LENGTH") or 0)
    payload = json.loads(environ["wsgi.input"].read(size) or b"{}")
    result = handle(payload)
  except ValueError as exc:
    result = {"error": f"Invalid JSON payload: {exc}"}

  body = json.dumps(result, default=str).encode("utf-8")
  start_response("200 OK", [
    ("Content-Type", "application/json"),
    ("Content-Length", str(len(body))),
  ])
  return [body]


def _handle_stdin() -> None:
  """Used when the server runs Python locally as a child process."""
  try:
    payload_raw = sys.stdin.read()
    if not payload_raw.strip():
      raise ValueError("Empty request payload")
    result = handle(json.loads(payload_raw))
  except ValueError as exc:
    result = {"error": str(exc)}

  json.dump(result, sys.stdout)


if __name__ == "__main__":
  _handle_stdin()
