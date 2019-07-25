import argparse
import os
import requests
from requests_oauthlib import OAuth1

def authorize_api_account():
    url = "https://api.twitter.com/1.1/account/verify_credentials.json"
    auth = OAuth1(
        os.getenv("TWITTER_RECURSE_API_KEY"),
        os.getenv("TWITTER_RECURSE_API_SECRET"),
        os.getenv("TWITTER_RECURSE_ACCESS_TOKEN"),
        os.getenv("TWITTER_RECURSE_ACCESS_TOKEN_SECRET"),
    )
    requests.get(url, auth=auth)
    return auth


def get_tweets(user, auth, num_tweets=100):
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={}&count={}".format(
        user, num_tweets
    )
    r = requests.get(url, auth=auth)
    return [tweet["text"] for tweet in r.json()]


def store_tweets(tweets, output_filepath):
    with open(output_filepath, "w") as fh:
        fh.write("\n".join(tweets))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pull tweets from one user.")
    parser.add_argument(
        "--num_tweets", type=int, default=10, help="How many tweets should we pull?"
    )
    parser.add_argument(
        "--account", type=str, help="The Twitter user account from which to pull."
    )
    parser.add_argument(
        "--output", type=str, help="A path to which to write line-separated tweets."
    )
    args = parser.parse_args()
    print("Authorizing Twitter API account.")
    auth = authorize_api_account()
    print("Pulling {} latest tweets from {}".format(args.num_tweets, args.account))
    tweets = get_tweets(args.account, auth, num_tweets=args.num_tweets)
    print("Writing tweets to {}".format(args.output))
    store_tweets(tweets, args.output)
