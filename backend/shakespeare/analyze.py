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

def build_combined_shakespeare_model(models):
    combined_model = None
    for model in models:
        if not combined_model:
            combined_model = model
        else:
            combined_model = combine_models([combined_model, model])
    write_model(combined_model, name=shakespeare_model_name("combined"))

def shakespeare_model_name(archetype):
    return "#{}".format(archetype)

def load_shakespeare_model(archetype):
    return load_model(shakespeare_model_name(archetype))
