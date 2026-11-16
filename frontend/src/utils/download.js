function downloadBlob(content, type, filename) {
  const blob = new Blob([content], { type });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  link.click();
  URL.revokeObjectURL(url);
}

function escapeCsv(value) {
  const str = String(value ?? "").replace(/"/g, '""');
  return /[",\n]/.test(str) ? `"${str}"` : str;
}

export function downloadCsv(rows, filename = "synthetic-data.csv") {
  if (!rows.length) return;
  const headers = Object.keys(rows[0]);
  const lines = [
    headers.join(","),
    ...rows.map((row) => headers.map((h) => escapeCsv(row[h])).join(",")),
  ];
  downloadBlob(lines.join("\n"), "text/csv;charset=utf-8;", filename);
}

export function downloadJson(rows, filename = "synthetic-data.json") {
  if (!rows.length) return;
  downloadBlob(JSON.stringify(rows, null, 2), "application/json;charset=utf-8;", filename);
}
