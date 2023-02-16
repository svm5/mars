from flask import Flask, render_template


app = Flask(__name__)


@app.route("/<title>")
@app.route("/index/<title>")
def index(title):
    return render_template("base.html", title=title)


@app.route("/traning/<prof>")
def proff(prof):
    return render_template("training.html", prof=prof.lower())


@app.route("/list_prof/<list_type>")
def list_proff(list_type):
    if list_type.lower() not in ("ol", "ul"):
        return "Некорректный параметр (Введите ol или ul)"
    arr = ["Программист", "Доктор", "Инженер", "Пилот", "Эколог"]
    return render_template("list_prof.html", prof_list=arr, list_type=list_type)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)