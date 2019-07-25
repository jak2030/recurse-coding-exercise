import os

from flask import Flask, jsonify

from model.spacy_markov import SpacyMarkovify

MARKOV_MODEL_PATH = os.getenv("MARKOV_MODEL_PATH")
with open(MARKOV_MODEL_PATH) as fh:
    model_json = fh.read()
    model = SpacyMarkovify.from_json(model_json)

app = Flask(__name__)


@app.route("/laws")
def get_law():
    law = model.make_short_sentence(280)
    return jsonify(law)
