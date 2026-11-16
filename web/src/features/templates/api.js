export async function fetchTemplates() {
  const res = await fetch("/api/templates");
  if (!res.ok) throw new Error("Failed to load templates");
  const data = await res.json();
  return data.templates || [];
}
