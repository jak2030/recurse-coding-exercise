import os

import markovify
import spacy

from util import make_missing_paths
from constants import MODELS_DIR

nlp = spacy.load("en")


class SpacyMarkovify(markovify.Text):
    """
    This extends some of the markovify methods for better text parsing.
    This example is from the readme: https://github.com/jsvine/markovify
    """

    def word_split(self, sentence):
        return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence

    @classmethod
    def combine(self, models, weights):
        return markovify.combine(models, weights)


class Reader(object):
    def __init__(self, root_dir):
        self.model_dir = root_dir

    def _model_path(self, model_name):
        return os.path.join(self.model_dir, model_name)

    def exists(self, model_name):
        fpath = self._model_path(model_name)
        return os.path.exists(fpath)

    def read(self, model_name):
        fpath = self._model_path(model_name)
        with open(fpath) as fh:
            model_json = fh.read()
        return SpacyMarkovify.from_json(model_json)


def combine_models(models, weights=None):
    return SpacyMarkovify.combine(models, weights)


def generate_model(text):
    """Generate a markov-chain model given a corpus."""
    model = SpacyMarkovify(text)
    return model


def write_model(model, name=None):
    """Serialize a model to json and write it to a file."""
    if not name:
        raise Exception("Name required for model.")
    model_json = model.to_json()
    fpath = os.path.join(MODELS_DIR, name)
    print("Writing model to {}".format(fpath))
    with open(fpath, "w") as fh:
        fh.write(model_json)


def load_model(model_name):
    reader = Reader(MODELS_DIR)
    model = reader.read(model_name)
    return model


def model_name(account, archetype):
    return "{}-{}".format(account, archetype)
