from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        print(1234)
        phone = request.form['phone']
        text = request.form['text']
        proxy = request.form['proxy']
        try:
            resp = requests.post('https://textbelt.com/text', {
                'phone': phone,
                'message': text,
                'key': 'textbelt_test',
            }, proxies={"http": proxy, "https": proxy})
            if resp.json()["success"]:
                return redirect("/success")
            else:
                return redirect("/limit")
        except Exception as e:
            return redirect("/wrong_data")
    else:
        return render_template("index.html")


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/wrong_data")
def wrong_data():
    return render_template("wrong_data.html")


@app.route("/limit")
def limit():
    return render_template("limit.html")


if __name__ == "__main__":
    app.run(debug=False)
