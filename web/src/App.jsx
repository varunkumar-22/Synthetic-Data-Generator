import { Routes, Route } from "react-router-dom";
import Sidebar from "./components/Sidebar/Sidebar";
import HomePage from "./features/home/HomePage";
import GeneratePage from "./features/generate/GeneratePage";
import TemplatesPage from "./features/templates/TemplatesPage";
import DocsPage from "./features/docs/DocsPage";
import useTemplates from "./features/templates/useTemplates";

export default function App() {
  const { templates, loading, error } = useTemplates();

  return (
    <div className="app-shell">
      <Sidebar />
      <main className="app-content">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route
            path="/generate"
            element={
              <GeneratePage templates={templates} loadingTemplates={loading} templatesError={error} />
            }
          />
          <Route
            path="/templates"
            element={<TemplatesPage templates={templates} loading={loading} error={error} />}
          />
          <Route path="/docs" element={<DocsPage />} />
        </Routes>
      </main>
    </div>
  );
}
