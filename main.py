from flask import Flask, url_for, render_template
import requests

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=["POST", "GET"])
def home():
    if requests.method == "POST":
        print(requests.form)
    return render_template('/home.html')


app.run(debug=True)