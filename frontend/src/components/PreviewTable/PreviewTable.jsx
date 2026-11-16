import "./PreviewTable.css";

const PREVIEW_LIMIT = 10;

export default function PreviewTable({ rows }) {
  if (!rows.length) {
    return (
      <section className="card">
        <h2 className="card-title">Preview</h2>
        <p className="muted">
          No data yet. Configure your template and click <strong>Generate Data</strong>.
        </p>
      </section>
    );
  }

  const columns = Object.keys(rows[0]);

  return (
    <section className="card">
      <h2 className="card-title">Preview</h2>
      <div className="table-wrapper">
        <table className="preview-table">
          <thead>
            <tr>
              {columns.map((col) => (
                <th key={col}>{col}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {rows.slice(0, PREVIEW_LIMIT).map((row, idx) => (
              <tr key={idx}>
                {columns.map((col) => (
                  <td key={col}>{String(row[col] ?? "")}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      {rows.length > PREVIEW_LIMIT && (
        <p className="muted preview-note">
          Showing first {PREVIEW_LIMIT} of {rows.length} rows. Download CSV or JSON for the full
          dataset.
        </p>
      )}
    </section>
  );
}
