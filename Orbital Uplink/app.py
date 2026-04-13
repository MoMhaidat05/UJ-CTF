import os
from flask import Flask, Response, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/diagnostic", methods=["POST"])
def diagnostic():
    target = request.form.get("target_satellite", "")

    cmd = f"echo Executing diagnostic routine for: {target} && echo Status: Online"

    try:
        output = os.popen(cmd).read()
    except Exception as exc:
        output = str(exc)

    return Response(output, mimetype="text/plain")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False)
