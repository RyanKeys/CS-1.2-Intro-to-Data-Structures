from flask import Flask, render_template
from histogram import weighted_histogram
app = Flask(__name__)
source_text = "test.txt"
histo = weighted_histogram(source_text)


@app.route('/')
def index():
    return render_template("index.html", histo = histo)
