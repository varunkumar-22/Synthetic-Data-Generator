// Express only treats this as an error handler because it takes four arguments.
// eslint-disable-next-line no-unused-vars
function errorHandler(err, req, res, next) {
  console.error(`${req.method} ${req.originalUrl} failed:`, err.message);
  res.status(500).json({ error: err.message || "Something went wrong" });
}

module.exports = errorHandler;
