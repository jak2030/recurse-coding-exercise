import os

from flask import Flask, jsonify, request

from model.reader import Reader
from model.train import generate_model


app = Flask(__name__)
# TODO use Flask app.config
MODEL_DIR = os.getenv("MODEL_DIR")
model_reader = Reader(MODEL_DIR)

@app.route("/texts")
def get_text():
    twitter_username = request.args.get('username')
    if not model_reader.exists(twitter_username):
        model = run_etla(twitter_username, model_dir=MODEL_DIR)
    else:
        model = model_reader.read(twitter_username)
    text = model.make_short_sentence(280)
    formatted_text = " ".join(text.replace("\n", " ").split())
    return jsonify(formatted_text)
