from flask import Flask, render_template


app = Flask(__name__)


@app.route("/<title>")
@app.route("/index/<title>")
def index(title):
    return render_template("base.html", title=title)


@app.route("/traning/<prof>")
def proff(prof):
    return render_template("training.html", prof=prof.lower())


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)