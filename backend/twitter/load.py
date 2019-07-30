""" TODO NOT USING..."""

import os
import os
import errno
import sys 

from util import make_missing_paths

OUTPUT_DIR = os.getenv("BARDI_B_DATA_DIR")

def write_tweets(tweets, account, output_dir):
    tweets_dir = os.path.join(OUTPUT_DIR, "twitter", account + "/")
    print("Writing tweets to {}".format(tweets_dir))
    make_missing_paths(tweets_dir)
    for tweet in tweets:
        unique_id = "{id}_{created_at}".format(**tweet).replace(" ", "-")
        fpath = os.path.join(tweets_dir, unique_id)
        if os.path.exists(fpath):
            continue
        with open(fpath, "w") as fh:
            fh.write(tweet["text"])
