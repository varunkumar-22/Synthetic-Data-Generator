const { spawn } = require("child_process");
const { PYTHON, REPO_ROOT } = require("../config");

// Talks to forma/bridge.py over stdin/stdout.
function callPython(payload) {
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

module.exports = { callPython };
