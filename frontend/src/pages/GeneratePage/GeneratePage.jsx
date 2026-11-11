import { useMemo, useState } from "react";
import { useSearchParams } from "react-router-dom";
import PageHeader from "../../components/PageHeader/PageHeader";
import ConfigForm from "../../components/ConfigForm/ConfigForm";
import PreviewTable from "../../components/PreviewTable/PreviewTable";
import { generateData } from "../../api/client";
import { downloadCsv, downloadJson } from "../../utils/download";
import "./GeneratePage.css";

const DEFAULT_COUNT = 100;

export default function GeneratePage({ templates, loadingTemplates, templatesError }) {
  const [searchParams] = useSearchParams();
  const [selectedTemplateId, setSelectedTemplateId] = useState(searchParams.get("template") || "");
  const [selectedSubcats, setSelectedSubcats] = useState([]);
  const [count, setCount] = useState(DEFAULT_COUNT);
  const [seed, setSeed] = useState("");
  const [generating, setGenerating] = useState(false);
  const [error, setError] = useState("");
  const [rows, setRows] = useState([]);

  const currentTemplate = useMemo(
    () => templates.find((t) => t.id === selectedTemplateId),
    [templates, selectedTemplateId]
  );

  const handleTemplateChange = (id) => {
    setSelectedTemplateId(id);
    setSelectedSubcats([]);
  };

  const handleToggleSubcat = (name) => {
    setSelectedSubcats((prev) =>
      prev.includes(name) ? prev.filter((x) => x !== name) : [...prev, name]
    );
  };

  const handleGenerate = async (e) => {
    e.preventDefault();
    if (!selectedTemplateId || selectedSubcats.length === 0) {
      setError("Please select a template and at least one subcategory.");
      return;
    }

    setError("");
    setGenerating(true);
    try {
      const data = await generateData({
        templateId: selectedTemplateId,
        subcategories: selectedSubcats,
        count: Number(count),
        seed: seed || null,
      });
      setRows(data);
    } catch (e) {
      setError(e.message || "Failed to generate data");
    } finally {
      setGenerating(false);
    }
  };

  return (
    <>
      <PageHeader title="Generate" subtitle="Create fake datasets for testing and demos." />
      <div className="generate-layout">
        <ConfigForm
          templates={templates}
          loadingTemplates={loadingTemplates}
          selectedTemplateId={selectedTemplateId}
          onTemplateChange={handleTemplateChange}
          currentTemplate={currentTemplate}
          selectedSubcats={selectedSubcats}
          onToggleSubcat={handleToggleSubcat}
          count={count}
          onCountChange={setCount}
          seed={seed}
          onSeedChange={setSeed}
          error={error || templatesError}
          generating={generating}
          hasRows={rows.length > 0}
          onSubmit={handleGenerate}
          onDownloadCsv={() => downloadCsv(rows)}
          onDownloadJson={() => downloadJson(rows)}
        />
        <PreviewTable rows={rows} />
      </div>
    </>
  );
}
