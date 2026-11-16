const router = require("express").Router();
const { callPython } = require("../services/pythonBridge");

router.get("/", async (_req, res, next) => {
  try {
    res.json(await callPython({ action: "list_templates" }));
  } catch (err) {
    next(err);
  }
});

module.exports = router;
