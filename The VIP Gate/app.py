import os

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
FLAG = os.getenv("CTF_FLAG", "uj_ctf{vip_gate_url_parameter_manipulation_master}")


@app.route("/")
def index() -> str:
    return render_template("index.html")


@app.route("/api/flag")
def api_flag():
    status = request.args.get("status", "").strip().lower()

    if status == "vip":
        return jsonify({"flag": FLAG})

    return jsonify({"error": "access denied"}), 403


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    app.run(host="0.0.0.0", port=port, debug=False)
