from shakespeare.extract import parse_shakespeare
from shakespeare.load import write_shakespeare
from shakespeare.analyze import build_shakespeare_model
from model.spacy_markovify import generate_model, write_model, combine_models
from constants import VILLAINS, JESTERS, DREAMERS


def match(line, archetypes):
    for archetype in archetypes:
        if line["character"] == archetype["character"] and line["play"] == archetype["play"]:
            return True
    return False

def run_shakespeare_etl():
    print("Parsing the Bard...")
    villains = []
    jesters = []
    dreamers = []
    for line in parse_shakespeare():
        if match(line, VILLAINS):
            villains.append(line["text"])
        if match(line, JESTERS):
            jesters.append(line["text"])
        if match(line, DREAMERS):
            dreamers.append(line["text"])
    return dict(
        villain="\n".join(villains),
        jester="\n".join(jesters),
        dreamer="\n".join(dreamers),
    )


def build_combined_shakespeare_model(models):
    combined_model = None
    for model in models:
        if not combined_model:
            combined_model = model
        else:
            combined_model = combine_models([combined_model, model])
    write_model(combined_model, name="#combined")

def preprocess_shakespeare():
    lines = run_shakespeare_etl()
    models = []
    for archetype_name in lines:
        model_name = "#" + archetype_name
        print("Building Shakespeare model for {}.".format(model_name))
        model = build_shakespeare_model(lines[archetype_name], model_name)
        models.append(model)
    print("Building combined Shakespeare model.")
    build_combined_shakespeare_model(models)
   
    

if __name__ == "__main__":
    preprocess_shakespeare()
