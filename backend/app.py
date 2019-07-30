import os

from flask import Flask, jsonify, request

from model.spacy_markovify import Reader as ModelReader, model_name
from task import build_combined_model
from constants import MODELS_DIR

app = Flask(__name__)
model_reader = ModelReader(MODELS_DIR)


def quick_clean(txt):
    # remove trailing spaces from these characters
    txt = " ".join(txt.replace("\n", " ").split())
    for char in [" ,", " ;", " '"]:
        txt = txt.replace(char, char.replace(" ", ""))
    return txt


@app.route("/lines")
def get_text():
    twitter_username = request.args.get("username", "iamcardib")
    app.logger.info("Twitter name: {}".format(twitter_username))
    archetype = request.args.get("archetype", "jester").lower()
    name = model_name(twitter_username, archetype)
    if not model_reader.exists(name):
        app.logger.info(
            "Building new {} archetype model for Twitter account {}".format(
                archetype, twitter_username
            )
        )
        model = build_combined_model(twitter_username, archetype)
    else:
        model = model_reader.read(name)
    # Try to get a longer tweet...
    attempts = 3
    for _ in range(0, attempts):
        text = model.make_short_sentence(280)
        if len(text) > 100:
            break
    formatted_text = quick_clean(text)
    return jsonify(formatted_text)
