import os

from model.spacy_markovify import combine_models, load_model, generate_model, write_model
from constants import SHAKESPEARE_DATA_DIR
from util import crawl_for_text


def read_shakespeare():
    return crawl_for_text(SHAKESPEARE_DATA_DIR)


def build_shakespeare_model(lines, model_name):
    """
    Some non-mutually exclusive augmentations to more interesting models might be:
        - Improve categorization by archetypes. Make editorial decisions about the
        inclusion/exclusion of character from categories. Villain, jester, dreamer, etc.
        and also decide on a good set of categories to use.
        - Run all lines (or subsets of lines grouped into categories) through an ANN for a more
        artificially derived Shakespeare.
        - ...
    """
    model = generate_model(lines)
    write_model(model, model_name)
    return model



def load_shakespeare_model(archetype):
    return load_model("#" + archetype)
