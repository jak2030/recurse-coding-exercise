import argparse

from extract import run_extraction
from load import store_tweets

def run_etl(account, num_tweets=1000, output_dir=None):
    tweets = run_extraction(account, num_tweets=num_tweets) 
    print("Writing tweets to {}".format(output_dir))
    store_tweets(tweets, account, output_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pull tweets from one user.")
    parser.add_argument(
        "--num-tweets", type=int, default=10, help="How many tweets should we pull?"
    )
    parser.add_argument(
        "--account",
        type=str,
        help="The Twitter user account from which to pull.",
    )
    parser.add_argument(
        "--output-dir", type=str, help="A directory to which to write tweets."
    )
    args = parser.parse_args()
    run_etl(args.account, num_tweets=args.num_tweets, output_dir=args.output_dir)
