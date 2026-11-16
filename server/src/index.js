const app = require("./app");
const { PORT } = require("./config");

app.listen(PORT, () => {
  console.log(`Forma server listening on http://localhost:${PORT}`);
});
