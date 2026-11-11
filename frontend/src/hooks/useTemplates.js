import { useEffect, useState } from "react";
import { fetchTemplates } from "../api/client";

export default function useTemplates() {
  const [templates, setTemplates] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    fetchTemplates()
      .then(setTemplates)
      .catch((e) => setError(e.message || "Failed to load templates"))
      .finally(() => setLoading(false));
  }, []);

  return { templates, loading, error };
}
