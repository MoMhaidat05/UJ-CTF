import os

from flask import Flask, Response, render_template, request

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return render_template("index.html")


@app.route("/monitor")
def monitor() -> Response:
    feed = request.args.get("feed")

    if not feed:
        return Response("No feed specified.", status=400, mimetype="text/plain")

    if "." not in feed:
        feed = f"{feed}.jpg"

    target_path = os.path.join(app.root_path, "static", "images", feed)

    try:
        with open(target_path, "r", encoding="utf-8", errors="replace") as stream:
            content = stream.read()
            return Response(content, mimetype="text/plain")
    except Exception:
        return Response("Feed offline or file not found.", status=404, mimetype="text/plain")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False)