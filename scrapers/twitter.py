import argparse


def get_tweets(user, num_tweets=100):
    return "tweets tweets tweets."


def store_tweets(tweets, output_filepath):
    with open(output_filepath, "w") as fh:
        fh.write(tweets)


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
    print("Pulling {} latest tweets from {}".format(args.num_tweets, args.account))
    tweets = get_tweets(args.account, num_tweets=args.num_tweets)
    print("Writing tweets to {}".format(args.output))
    store_tweets(tweets, args.output)
