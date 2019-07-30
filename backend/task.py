import os
import random

from flask import current_app

from model.spacy_markovify import model_name, combine_models, generate_model, write_model
from twitter.extract import extract_tweets
from shakespeare.analyze import load_shakespeare_model
from constants import DATA_DIR

def _build_tweets_model(account, num_tweets):
    try:
        tweets = extract_tweets(account, num_tweets) 
    except Exception:
        raise
    tweets_txt = [tweet["text"] for tweet in tweets]
    model = generate_model(tweets_txt)
    return model

def build_combined_model(twitter_account, archetype):
    print("Making a combined model for {}".format(twitter_account))
    tweets_model = _build_tweets_model(twitter_account, num_tweets=1000)
    shakespeare_model = load_shakespeare_model(archetype)
    # TODO if more Shakespeare added/model size increased, then update weight
    # TODO experiment with weights
    combined_model = combine_models([ tweets_model, shakespeare_model ], [ 1, 1 ])
    write_model(combined_model, name=model_name(twitter_account, archetype))
    return combined_model


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Web app runtime tasks.")
    parser.add_argument(
        "--build-model",
        type=str,
        nargs="+",
        help="""Two arguments: The name of the Twitter account for which to build the model
        followed by the archetype they should talk like."""
    )
    # There's only one task, so just calling it here :)
    args = parser.parse_args()
    twitter_account = args.build_model[0]
    archetype = args.build_model[1]
    build_combined_model(twitter_account, archetype)

