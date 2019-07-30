from twitter.extract import extract_tweets
from model.spacy_markovify import generate_model


def build_tweets_model(account, num_tweets):
    try:
        tweets = extract_tweets(account, num_tweets)
    except Exception:
        raise
    tweets_txt = [tweet["text"] for tweet in tweets]
    model = generate_model(tweets_txt)
    return model
