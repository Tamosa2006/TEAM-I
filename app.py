import os
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

app = Flask(__name__)
CORS(app)
BASE = os.path.dirname(os.path.abspath(__file__))


@app.get("/")
def index():
    return send_from_directory(BASE, "index.html")


@app.get("/health")
def health():
    return jsonify(status="ok", project="Team I: PR Summarizer Bot", stack="flask")

@app.route("/webhook/github", methods=["POST"])
def ep_0(**kwargs):
    # TODO: GitHub webhook receiver
    return jsonify(error="Not implemented", todo="GitHub webhook receiver"), 501

@app.route("/api/summaries", methods=["GET"])
def ep_1(**kwargs):
    # TODO: List generated summaries
    return jsonify(error="Not implemented", todo="List generated summaries"), 501


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
