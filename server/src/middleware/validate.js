function validateGenerate(req, res, next) {
  const { templateId, subcategories, count } = req.body || {};

  if (!templateId) {
    return res.status(400).json({ error: "templateId is required" });
  }
  if (!Array.isArray(subcategories) || subcategories.length === 0) {
    return res
      .status(400)
      .json({ error: "subcategories (non-empty array) is required" });
  }
  if (!count || Number.isNaN(Number(count)) || Number(count) <= 0) {
    return res.status(400).json({ error: "count must be a positive integer" });
  }

  next();
}

module.exports = { validateGenerate };
