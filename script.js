try { require("dotenv").config(); } catch (e) {}
const express = require("express");
const cors = require("cors");
const path = require("path");

const app = express();
app.use(cors());
app.use(express.json());

app.get("/", (req, res) => res.sendFile(path.join(__dirname, "index.html")));

app.get("/health", (req, res) =>
  res.json({ status: "ok", project: "Team I: PR Summarizer Bot", stack: "node" })
);

app.post("/webhook/github", (req, res) => {
  // TODO: GitHub webhook receiver
  res.status(501).json({ error: "Not implemented", todo: "GitHub webhook receiver" });
});

app.get("/api/summaries", (req, res) => {
  // TODO: List generated summaries
  res.status(501).json({ error: "Not implemented", todo: "List generated summaries" });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Team I server running on http://localhost:${PORT}`));
