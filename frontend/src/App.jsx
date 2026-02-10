import React, { useEffect, useMemo, useState } from "react";

const DEFAULT_COUNT = 100;

export function App() {
  const [templates, setTemplates] = useState([]);
  const [selectedTemplateId, setSelectedTemplateId] = useState("");
  const [selectedSubcats, setSelectedSubcats] = useState([]);
  const [count, setCount] = useState(DEFAULT_COUNT);
  const [seed, setSeed] = useState("");
  const [loadingTemplates, setLoadingTemplates] = useState(false);
  const [loadingGenerate, setLoadingGenerate] = useState(false);
  const [error, setError] = useState("");
  const [rows, setRows] = useState([]);

  useEffect(() => {
    const loadTemplates = async () => {
      setLoadingTemplates(true);
      setError("");
      try {
        const res = await fetch("/api/templates");
        if (!res.ok) {
          throw new Error("Failed to load templates");
        }
        const data = await res.json();
        setTemplates(data.templates || []);
      } catch (e) {
        setError(e.message || "Failed to load templates");
      } finally {
        setLoadingTemplates(false);
      }
    };

    loadTemplates();
  }, []);

  const currentTemplate = useMemo(
    () => templates.find((t) => t.id === selectedTemplateId),
    [templates, selectedTemplateId]
  );

  const onToggleSubcat = (name) => {
    setSelectedSubcats((prev) =>
      prev.includes(name)
        ? prev.filter((x) => x !== name)
        : [...prev, name]
    );
  };

  const handleGenerate = async (e) => {
    e.preventDefault();
    if (!selectedTemplateId || selectedSubcats.length === 0) {
      setError("Please select a template and at least one subcategory.");
      return;
    }

    setError("");
    setLoadingGenerate(true);
    try {
      const body = {
        templateId: selectedTemplateId,
        subcategories: selectedSubcats,
        count: Number(count),
        seed: seed || null
      };
      const res = await fetch("/api/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body)
      });
      const data = await res.json();
      if (!res.ok || data.error) {
        throw new Error(data.error || "Failed to generate data");
      }
      setRows(data.rows || []);
    } catch (e) {
      setError(e.message || "Failed to generate data");
    } finally {
      setLoadingGenerate(false);
    }
  };

  const handleDownloadCsv = () => {
    if (!rows.length) return;
    const headers = Object.keys(rows[0]);
    const csvLines = [
      headers.join(","),
      ...rows.map((row) =>
        headers
          .map((h) => {
            const val = row[h] ?? "";
            const str = String(val).replace(/"/g, '""');
            return /[",\n]/.test(str) ? `"${str}"` : str;
          })
          .join(",")
      )
    ];
    const blob = new Blob([csvLines.join("\n")], {
      type: "text/csv;charset=utf-8;"
    });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = "synthetic-data.csv";
    link.click();
    URL.revokeObjectURL(url);
  };

  const handleDownloadJson = () => {
    if (!rows.length) return;
    const blob = new Blob([JSON.stringify(rows, null, 2)], {
      type: "application/json;charset=utf-8;"
    });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = "synthetic-data.json";
    link.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="app-root">
      <header className="app-header">
        <h1>Synthetic Data Generator</h1>
        <p>Create rich, fake datasets for testing and demos.</p>
      </header>

      <main className="app-main">
        <section className="card">
          <h2>Configuration</h2>

          {error && <div className="alert alert-error">{error}</div>}

          <form className="form-grid" onSubmit={handleGenerate}>
            <div className="field">
              <label>Template</label>
              <select
                value={selectedTemplateId}
                onChange={(e) => {
                  setSelectedTemplateId(e.target.value);
                  setSelectedSubcats([]);
                }}
                disabled={loadingTemplates}
              >
                <option value="">
                  {loadingTemplates ? "Loading templates..." : "Select template"}
                </option>
                {templates.map((t) => (
                  <option key={t.id} value={t.id}>
                    {t.name}
                  </option>
                ))}
              </select>
            </div>

            <div className="field">
              <label>Rows to generate</label>
              <input
                type="number"
                min="1"
                value={count}
                onChange={(e) => setCount(e.target.value)}
              />
            </div>

            <div className="field">
              <label>Seed (optional)</label>
              <input
                type="number"
                placeholder="e.g. 42"
                value={seed}
                onChange={(e) => setSeed(e.target.value)}
              />
            </div>

            <div className="field field-full">
              <label>Subcategories</label>
              {!currentTemplate && (
                <p className="muted">
                  Select a template to see its subcategories.
                </p>
              )}
              {currentTemplate && (
                <div className="chips">
                  {currentTemplate.subcategories.map((sub) => (
                    <button
                      key={sub}
                      type="button"
                      className={
                        selectedSubcats.includes(sub)
                          ? "chip chip-selected"
                          : "chip"
                      }
                      onClick={() => onToggleSubcat(sub)}
                    >
                      {sub}
                    </button>
                  ))}
                </div>
              )}
            </div>

            <div className="actions">
              <button
                type="submit"
                className="btn btn-primary"
                disabled={loadingGenerate}
              >
                {loadingGenerate ? "Generating..." : "Generate Data"}
              </button>
            </div>

            <div className="actions actions-secondary">
              <button
                type="button"
                className="btn"
                onClick={handleDownloadCsv}
                disabled={!rows.length}
              >
                Download CSV
              </button>
              <button
                type="button"
                className="btn"
                onClick={handleDownloadJson}
                disabled={!rows.length}
              >
                Download JSON
              </button>
            </div>
          </form>
        </section>

        <section className="card">
          <h2>Preview</h2>
          {!rows.length && (
            <p className="muted">
              No data yet. Configure your template and click{" "}
              <strong>Generate Data</strong>.
            </p>
          )}
          {rows.length > 0 && (
            <div className="table-wrapper">
              <table>
                <thead>
                  <tr>
                    {Object.keys(rows[0]).map((key) => (
                      <th key={key}>{key}</th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {rows.slice(0, 10).map((row, idx) => (
                    <tr key={idx}>
                      {Object.keys(rows[0]).map((key) => (
                        <td key={key}>{String(row[key] ?? "")}</td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
              {rows.length > 10 && (
                <p className="muted">
                  Showing first 10 of {rows.length} rows. Download CSV or JSON
                  for the full dataset.
                </p>
              )}
            </div>
          )}
        </section>
      </main>
    </div>
  );
}

