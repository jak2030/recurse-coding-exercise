import argparse
import os
import errno

import requests
from requests_oauthlib import OAuth1


def authorize_api_account():
    url = "https://api.twitter.com/1.1/account/verify_credentials.json"
    auth = OAuth1(
        os.getenv("TWITTER_API_KEY"),
        os.getenv("TWITTER_API_SECRET"),
        os.getenv("TWITTER_ACCESS_TOKEN"),
        os.getenv("TWITTER_ACCESS_TOKEN_SECRET"),
    )
    requests.get(url, auth=auth)
    return auth


def get_tweets(users, auth, num_tweets=100, max_id=0):
    max_tweets_per_call = 200
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    tweets = []
    for user in users:
        cur_tweet_count = 0
        params = dict(
            screen_name=user,
            count=num_tweets if num_tweets < max_tweets_per_call else max_tweets_per_call,
        )
        while cur_tweet_count < num_tweets:
            if len(tweets):
                params["max_id"] = tweets[-1]["id"]
            r = requests.get(url, params=params, auth=auth)
            batch = [tweet for tweet in r.json()]
            tweets.extend(batch)
            cur_tweet_count += len(batch)
    return tweets


def store_tweets(tweets, output_dir):
    if not os.path.exists(os.path.dirname(output_dir)):
        try:
            os.makedirs(os.path.dirname(output_dir))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    for tweet in tweets:
        unique_id = "{id}_{created_at}".format(**tweet).replace(" ", "-")
        output_fpath = os.path.join(output_dir, unique_id)
        with open(output_fpath, "w") as fh:
            fh.write(tweet["text"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pull tweets from one user.")
    parser.add_argument(
        "--num-tweets", type=int, default=10, help="How many tweets should we pull?"
    )
    parser.add_argument(
        "--accounts",
        type=str,
        nargs="+",
        help="The Twitter user account from which to pull.",
    )
    parser.add_argument(
        "--output-dir", type=str, help="A directory to which to write tweets."
    )
    args = parser.parse_args()
    print("Authorizing Twitter API account.")
    auth = authorize_api_account()
    print("Pulling {} latest tweets from {}".format(args.num_tweets, args.accounts))
    tweets = get_tweets(args.accounts, auth, num_tweets=args.num_tweets)
    print("Writing tweets to {}".format(args.output_dir))
    store_tweets(tweets, args.output_dir)
