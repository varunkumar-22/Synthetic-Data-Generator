const express = require("express");
const cors = require("cors");
const { spawn } = require("child_process");
const path = require("path");

const app = express();
const PORT = process.env.PORT || 4000;

app.use(cors());
app.use(express.json());

// Small helper to talk to the Python bridge using stdin/stdout.
function callPythonApi(payload) {
  return new Promise((resolve, reject) => {
    const repoRoot = path.join(__dirname, "..", "..");

    // Prefer PYTHON env var if set, fall back to python3, then python
    const pythonCmd = process.env.PYTHON || "python3";

    const py = spawn(pythonCmd, ["-m", "structured_data_generator.api"], {
      cwd: repoRoot
    });

    let stdout = "";
    let stderr = "";

    py.stdout.on("data", (data) => {
      stdout += data.toString();
    });

    py.stderr.on("data", (data) => {
      stderr += data.toString();
    });

    py.on("error", (err) => {
      reject(err);
    });

    py.on("close", () => {
      // If Python printed anything to stderr or nothing to stdout,
      // treat it as an error so we can see the real message.
      if (stderr.trim() || !stdout.trim()) {
        const msg = `Python bridge failed. stdout="${stdout.trim()}", stderr="${stderr.trim()}"`;
        return reject(new Error(msg));
      }

      try {
        const json = JSON.parse(stdout || "{}");
        return resolve(json);
      } catch (e) {
        const msg = `Could not parse Python output. stdout="${stdout}", stderr="${stderr}"`;
        return reject(new Error(msg));
      }
    });

    py.stdin.write(JSON.stringify(payload));
    py.stdin.end();
  });
}

app.get("/api/health", (_req, res) => {
  res.json({ status: "ok" });
});

app.get("/api/templates", async (_req, res) => {
  try {
    const result = await callPythonApi({ action: "list_templates" });
    res.json(result);
  } catch (err) {
    console.error("Error loading templates:", err.message);
    res.status(500).json({ error: err.message || "Failed to load templates" });
  }
});

app.post("/api/generate", async (req, res) => {
  const { templateId, subcategories, count, seed } = req.body || {};

  if (!templateId) {
    return res.status(400).json({ error: "templateId is required" });
  }
  if (!Array.isArray(subcategories) || subcategories.length === 0) {
    return res
      .status(400)
      .json({ error: "subcategories (non-empty array) is required" });
  }
  if (!count || Number.isNaN(Number(count)) || Number(count) <= 0) {
    return res
      .status(400)
      .json({ error: "count must be a positive integer" });
  }

  try {
    const payload = {
      action: "generate",
      templateId,
      subcategories,
      count: Number(count),
      seed: seed === undefined || seed === null || seed === "" ? null : seed
    };

    const result = await callPythonApi(payload);
    res.json(result);
  } catch (err) {
    console.error("Error generating data:", err.message);
    res.status(500).json({ error: err.message || "Failed to generate data" });
  }
});

app.listen(PORT, () => {
  // eslint-disable-next-line no-console
  console.log(`Synthetic Data backend listening on http://localhost:${PORT}`);
});

