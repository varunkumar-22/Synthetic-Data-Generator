const app = require("./app");
const { PORT } = require("./config");

app.listen(PORT, () => {
  console.log(`Synthetic Data backend listening on http://localhost:${PORT}`);
});
