# import the required libraries
from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def gen_quote():
    URL = "https://api.quotable.io/random"

    # get the url from required website
    response = requests.get(URL)
    data = response.json()

    quote = data['content']
    author = data['author']

    return render_template('index.html', quote=quote, author=author)


if __name__ == "__main__":
    app.run(debug=True)
