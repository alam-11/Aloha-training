from flask import Flask, render_template, request
import json

app = Flask(__name__)

fp = open('countries.json')
countries = json.load(fp)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/", methods=["GET", "POST"])
def cities():
    if request.method == "POST":
        # try:
            country = request.form.get("country")
            list_cities = list(countries[country])
            return render_template('index.html',searched = country,foobar=list_cities)
        # except:
        #     return "<p>coundn't process</p>"


if __name__ == "__main__":
    app.run(debug=True)
