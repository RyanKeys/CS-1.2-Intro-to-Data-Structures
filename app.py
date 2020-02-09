from flask import Flask, render_template
from histogram import Dictogram
app = Flask(__name__)
source_text = "test.txt"
histo = Dictogram()
histo = histo.histogram(source_text)


@app.route('/')
def index():
    return render_template("index.html", histo = histo)
