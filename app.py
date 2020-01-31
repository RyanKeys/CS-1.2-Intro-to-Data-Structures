from flask import Flask
from histogram import weighted_histogram
app = Flask(__name__)
source_text = "test.txt"
histo = str(weighted_histogram(source_text))


@app.route('/')
def index():
    return histo
