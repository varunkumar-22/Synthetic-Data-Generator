import "./TemplateCard.css";

export default function TemplateCard({ template, onUse }) {
  return (
    <article className="card template-card">
      <div className="template-card-head">
        <h2 className="template-card-title">{template.name}</h2>
        <span className="template-card-count">
          {template.subcategories.length} subcategories
        </span>
      </div>
      <ul className="template-card-list">
        {template.subcategories.map((sub) => (
          <li key={sub} className="template-card-item">
            {sub}
          </li>
        ))}
      </ul>
      <button type="button" className="btn btn-primary template-card-action" onClick={onUse}>
        Use template
      </button>
    </article>
  );
}
