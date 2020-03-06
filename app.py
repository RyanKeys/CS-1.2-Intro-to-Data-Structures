from flask import Flask, render_template
from markov import MarkovChain
from cleanup import cleanup
app = Flask(__name__)
source_text = cleanup("trump.txt")
markov = MarkovChain(source_text)

@app.route('/')
def index():
    return render_template("index.html", markov = markov)
