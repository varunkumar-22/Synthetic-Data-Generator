import Alert from "../Alert/Alert";
import SubcategoryPicker from "../SubcategoryPicker/SubcategoryPicker";
import "./ConfigForm.css";

export default function ConfigForm({
  templates,
  loadingTemplates,
  selectedTemplateId,
  onTemplateChange,
  currentTemplate,
  selectedSubcats,
  onToggleSubcat,
  count,
  onCountChange,
  seed,
  onSeedChange,
  error,
  generating,
  hasRows,
  onSubmit,
  onDownloadCsv,
  onDownloadJson,
}) {
  return (
    <section className="card">
      <h2 className="card-title">Configuration</h2>
      <Alert>{error}</Alert>

      <form className="form-grid" onSubmit={onSubmit}>
        <div className="field field-full">
          <label className="field-label">Template</label>
          <select
            className="field-input"
            value={selectedTemplateId}
            onChange={(e) => onTemplateChange(e.target.value)}
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
          <label className="field-label">Rows to generate</label>
          <input
            className="field-input"
            type="number"
            min="1"
            value={count}
            onChange={(e) => onCountChange(e.target.value)}
          />
        </div>

        <div className="field">
          <label className="field-label">Seed (optional)</label>
          <input
            className="field-input"
            type="number"
            placeholder="e.g. 42"
            value={seed}
            onChange={(e) => onSeedChange(e.target.value)}
          />
        </div>

        <div className="field field-full">
          <label className="field-label">Subcategories</label>
          <SubcategoryPicker
            options={currentTemplate?.subcategories}
            selected={selectedSubcats}
            onToggle={onToggleSubcat}
          />
        </div>

        <div className="form-actions">
          <button type="submit" className="btn btn-primary" disabled={generating}>
            {generating ? "Generating..." : "Generate Data"}
          </button>
          <button type="button" className="btn" onClick={onDownloadCsv} disabled={!hasRows}>
            Download CSV
          </button>
          <button type="button" className="btn" onClick={onDownloadJson} disabled={!hasRows}>
            Download JSON
          </button>
        </div>
      </form>
    </section>
  );
}
