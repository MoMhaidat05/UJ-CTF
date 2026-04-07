from flask import Flask, make_response, render_template, request

FLAG = "uj_ctf{c00k1e_m4n1pul4t10n_m4st3r}"

app = Flask(__name__)


@app.route("/")
def index():
    user_type = request.cookies.get("user_type")

    response = make_response(render_template("index.html", user_type=user_type or "guest"))
    if user_type is None:
        response.set_cookie("user_type", "guest", samesite="Lax")

    return response


@app.route("/admin")
def admin_panel():
    user_type = request.cookies.get("user_type")

    if user_type == "admin":
        return render_template("admin.html", is_admin=True, flag=FLAG), 200

    return render_template("admin.html", is_admin=False), 403


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
