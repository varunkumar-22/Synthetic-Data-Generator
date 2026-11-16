const router = require("express").Router();
const { callPython } = require("../services/pythonBridge");
const { validateGenerate } = require("../middleware/validate");

router.post("/", validateGenerate, async (req, res, next) => {
  const { templateId, subcategories, count, seed } = req.body;

  try {
    const result = await callPython({
      action: "generate",
      templateId,
      subcategories,
      count: Number(count),
      seed: seed === undefined || seed === null || seed === "" ? null : seed,
    });
    res.json(result);
  } catch (err) {
    next(err);
  }
});

module.exports = router;
