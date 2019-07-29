import os

from spacy_markov import SpacyMarkovify


class Reader(object):
    def __init__(self, root_dir):
        self.model_dir = os.path.join(root_dir, "models")

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
