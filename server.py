from flask import Flask
from histogram import histogram
app = Flask(__name__)
source_text = "test.txt"
histo = str(histogram(source_text))


@app.route('/')
def index():
    return histo
