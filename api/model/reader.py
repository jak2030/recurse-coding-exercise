import os

from spacy_markov import SpacyMarkovify


class Reader(object):
    def __init__(self, corpus_dir):
        self.corpus_dir = corpus_dir

    def _model_path(self, model_name):
        return os.path.join(self.corpus_dir, model_name)

    def exists(self, model_name):
        fpath = self._model_path(model_name)
        return os.path.exists(fpath)

    def read(self, model_name):
        fpath = self._model_path(model_name)
        with open(fpath) as fh:
            model_json = fh.read()
        return SpacyMarkovify.from_json(model_json)
