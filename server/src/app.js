const express = require("express");
const cors = require("cors");
const errorHandler = require("./middleware/errorHandler");

const app = express();

app.use(cors());
app.use(express.json());

// Each feature gets its own file in routes/ and one line here.
app.use("/api/health", require("./routes/health"));
app.use("/api/templates", require("./routes/templates"));
app.use("/api/generate", require("./routes/generate"));

app.use(errorHandler);

module.exports = app;
