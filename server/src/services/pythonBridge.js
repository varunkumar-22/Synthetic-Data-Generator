const { spawn } = require("child_process");
const { PYTHON, REPO_ROOT, PYTHON_SERVICE_URL } = require("../config");

// On Vercel, Python runs as its own service and we call it over HTTP.
async function callPythonService(payload) {
  const res = await fetch(PYTHON_SERVICE_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  const text = await res.text();
  try {
    return JSON.parse(text);
  } catch (e) {
    throw new Error(`Python service returned ${res.status}: ${text.slice(0, 200)}`);
  }
}

// Locally, run forma/bridge.py as a child process over stdin/stdout.
function callPythonProcess(payload) {
  return new Promise((resolve, reject) => {
    const py = spawn(PYTHON, ["-m", "forma.bridge"], {
      cwd: REPO_ROOT,
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
        return resolve(JSON.parse(stdout));
      } catch (e) {
        const msg = `Could not parse Python output. stdout="${stdout}", stderr="${stderr}"`;
        return reject(new Error(msg));
      }
    });

    py.stdin.write(JSON.stringify(payload));
    py.stdin.end();
  });
}

async function callPython(payload) {
  const result = PYTHON_SERVICE_URL
    ? await callPythonService(payload)
    : await callPythonProcess(payload);

  // The bridge reports its own errors as {"error": "..."}
  if (result && result.error) {
    throw new Error(result.error);
  }
  return result;
}

module.exports = { callPython };
