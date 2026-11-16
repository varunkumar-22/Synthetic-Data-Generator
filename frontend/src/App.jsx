import { Routes, Route } from "react-router-dom";
import Sidebar from "./components/Sidebar/Sidebar";
import HomePage from "./pages/HomePage/HomePage";
import GeneratePage from "./pages/GeneratePage/GeneratePage";
import TemplatesPage from "./pages/TemplatesPage/TemplatesPage";
import DocsPage from "./pages/DocsPage/DocsPage";
import useTemplates from "./hooks/useTemplates";

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
