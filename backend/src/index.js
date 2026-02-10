const express = require("express");
const cors = require("cors");
const { spawn } = require("child_process");
const path = require("path");

const app = express();
const PORT = process.env.PORT || 4000;

app.use(cors());
app.use(express.json());

function callPythonApi(payload) {
  return new Promise((resolve, reject) => {
    // Run Python from the repo root so the structured_data_generator
    // package can be imported without needing a pip install.
    const repoRoot = path.join(__dirname, "..", "..");
    const py = spawn("python", ["-m", "structured_data_generator.api"], {
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
      if (stderr) {
        // Python module prints errors to JSON on stdout; stderr here is unexpected
        // but surface it just in case.
        console.error("Python stderr:", stderr);
      }

      try {
        const json = JSON.parse(stdout || "{}");
        resolve(json);
      } catch (e) {
        reject(
          new Error(
            `Failed to parse Python response. Raw output: ${stdout}\nError: ${e.message}`
          )
        );
      }
    });

    py.stdin.write(JSON.stringify(payload));
    py.stdin.end();
  });
}

app.get("/api/templates", async (_req, res) => {
  try {
    const result = await callPythonApi({ action: "list_templates" });
    if (result.error) {
      return res.status(500).json({ error: result.error });
    }
    return res.json(result);
  } catch (err) {
    console.error(err);
    return res
      .status(500)
      .json({ error: `Failed to load templates: ${err.message}` });
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
    if (result.error) {
      return res.status(500).json({ error: result.error });
    }
    return res.json(result);
  } catch (err) {
    console.error(err);
    return res.status(500).json({ error: "Failed to generate data" });
  }
});

app.get("/api/health", (_req, res) => {
  res.json({ status: "ok" });
});

app.listen(PORT, () => {
  // eslint-disable-next-line no-console
  console.log(`Synthetic Data backend listening on http://localhost:${PORT}`);
});

