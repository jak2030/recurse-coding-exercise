import os

from flask import Flask, jsonify

from model.spacy_markov import SpacyMarkovify

MARKOV_MODEL_PATH = os.getenv("MARKOV_MODEL_PATH")
with open(MARKOV_MODEL_PATH) as fh:
    model_json = fh.read()
    model = SpacyMarkovify.from_json(model_json)

app = Flask(__name__)


@app.route("/texts")
def get_text():
    text = model.make_short_sentence(280)
    formatted_text = " ".join(text.replace("\n", " ").split())
    return jsonify(formatted_text)
