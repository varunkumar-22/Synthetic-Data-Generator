import { useNavigate } from "react-router-dom";
import PageHeader from "../../components/PageHeader/PageHeader";
import Alert from "../../components/Alert/Alert";
import TemplateCard from "../../components/TemplateCard/TemplateCard";
import "./TemplatesPage.css";

export default function TemplatesPage({ templates, loading, error }) {
  const navigate = useNavigate();

  return (
    <>
      <PageHeader
        title="Templates"
        subtitle="Pre-defined templates and the subcategories of data each one can generate."
      />
      <Alert>{error}</Alert>
      {loading && <p className="muted">Loading templates...</p>}
      <div className="templates-grid">
        {templates.map((t) => (
          <TemplateCard key={t.id} template={t} onUse={() => navigate(`/generate?template=${encodeURIComponent(t.id)}`)} />
        ))}
      </div>
    </>
  );
}
