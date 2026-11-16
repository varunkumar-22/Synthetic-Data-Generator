const path = require("path");

module.exports = {
  PORT: process.env.PORT || 4000,
  // Set PYTHON to point at a virtualenv interpreter if needed
  PYTHON: process.env.PYTHON || "python3",
  REPO_ROOT: path.join(__dirname, "..", ".."),
};
