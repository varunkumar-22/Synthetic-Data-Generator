const path = require("path");

module.exports = {
  PORT: process.env.PORT || 4000,
  // Set PYTHON to point at a virtualenv interpreter if needed
  PYTHON: process.env.PYTHON || "python3",
  REPO_ROOT: path.join(__dirname, "..", ".."),
  // Set by Vercel through the binding in vercel.json. Unset locally.
  PYTHON_SERVICE_URL: process.env.PYTHON_SERVICE_URL,
};
