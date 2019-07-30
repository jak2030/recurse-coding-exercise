from shakespeare.extract import parse_by_category
from shakespeare.analyze import (
    shakespeare_model_name,
    build_combined_shakespeare_model,
    build_shakespeare_model,
)


def run_shakespeare_etla():
    print("Parsing the Bard...")
    # where lines key -> val is archetype -> text_blob 
    lines = parse_by_category()
    models = []
    for archetype_name in lines:
        model_name = shakespeare_model_name(archetype_name)
        print("Building Shakespeare model for {}.".format(model_name))
        model = build_shakespeare_model(lines[archetype_name], model_name)
        models.append(model)
    print("Building combined Shakespeare model.")
    build_combined_shakespeare_model(models)
