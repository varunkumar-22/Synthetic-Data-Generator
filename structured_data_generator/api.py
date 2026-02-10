import json
import sys
from typing import Any, Dict, List, Optional

from scripts.generate_dataset import TEMPLATES
from structured_data_generator.core.generators import generate_from_template


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


def _handle_stdin() -> None:
  """
  Simple JSON-over-stdin/stdout protocol so other runtimes
  (like a Node.js backend) can call this module safely.

  Expected input JSON:
      {"action": "list_templates"}
  or:
      {
        "action": "generate",
        "templateId": "<template name>",
        "subcategories": ["User Info", "Device Info"],
        "count": 100,
        "seed": 42   # optional
      }
  """
  try:
    payload_raw = sys.stdin.read()
    if not payload_raw.strip():
      raise ValueError("Empty request payload")

    payload = json.loads(payload_raw)
    action = payload.get("action")

    if action == "list_templates":
      result = {"templates": get_templates_metadata()}
    elif action == "generate":
      template_id = payload["templateId"]
      subcats = payload.get("subcategories") or []
      count = int(payload.get("count", 1))
      seed = payload.get("seed")
      if seed is not None:
        seed = int(seed)

      rows = generate_data(template_id, subcats, count, seed)
      result = {"rows": rows}
    else:
      raise ValueError(f"Unknown action: {action}")

    json.dump(result, sys.stdout)
  except Exception as exc:  # noqa: BLE001
    # Keep the error payload JSON so callers can surface it nicely
    error_payload = {"error": str(exc)}
    json.dump(error_payload, sys.stdout)


if __name__ == "__main__":
  _handle_stdin()

