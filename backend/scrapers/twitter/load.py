import os
import os
import errno
import sys


def store_tweets(tweets, account, root_dir):
    print("Writing tweets to {}".format(output_dir))
    tweets_dir = os.path.join(root_dir, account)
    if not os.path.exists(os.path.dirname(tweets_dir)):
        try:
            os.makedirs(os.path.dirname(tweets_dir))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    for tweet in tweets:
        unique_id = "{id}_{created_at}".format(**tweet).replace(" ", "-")
        output_fpath = os.path.join(root_dir, unique_id)
        with open(output_fpath, "w") as fh:
            fh.write(tweet["text"])
