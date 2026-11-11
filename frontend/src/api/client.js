export async function fetchTemplates() {
  const res = await fetch("/api/templates");
  if (!res.ok) throw new Error("Failed to load templates");
  const data = await res.json();
  return data.templates || [];
}

export async function generateData(payload) {
  const res = await fetch("/api/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  const data = await res.json();
  if (!res.ok || data.error) {
    throw new Error(data.error || "Failed to generate data");
  }
  return data.rows || [];
}
