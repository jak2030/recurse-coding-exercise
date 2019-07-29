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
    try:
        r = requests.get(url, auth=auth)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    return auth


def get_tweets(account, auth, num_tweets=100, max_id=0):
    max_tweets_per_call = 200
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    params = dict(
        screen_name=account,
        count=num_tweets if num_tweets < max_tweets_per_call else max_tweets_per_call,
    )
    tweets = []
    cur_tweet_count = 0
    while cur_tweet_count < num_tweets:
        if len(tweets):
            params["max_id"] = tweets[-1]["id"]
        r = requests.get(url, params=params, auth=auth)
        batch = [tweet for tweet in r.json()]
        tweets.extend(batch)
        cur_tweet_count += len(batch)
    return tweets

def run_extraction(account, num_tweets):
    print("Authorizing Twitter API account.")
    auth = authorize_api_account()
    print("Pulling {} latest tweets from {}".format(num_tweets, account))
    tweets = get_tweets(account, auth, num_tweets=num_tweets)
    return tweets