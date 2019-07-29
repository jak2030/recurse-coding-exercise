import argparse
import re
import glob

from spacy_markov import SpacyMarkovify
from writer import Writer

def generate_model(corpus_dir):
    """Generate a markov model given a corpus."""
    text = []
    # remove a trailing slash and add asterisk
    glob_pattern = "{}/*".format("/".join(corpus_dir.split("/")[0:-1]))
    # combine text from all globbed files
    for fpath in glob.glob(glob_pattern):
        with open(fpath) as fh:
            text.append(fh.read())
    text_model = SpacyMarkovify("\n".join(text))
    return text_model


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a Markov model.")
    parser.add_argument(
        "--corpus-dir", type=str, help="A path to the corpus directory used for training."
    )
    parser.add_argument(
        "--output",
        type=str,
        help="A path to which to write a serialized version of the model.",
    )
    parser.add_argument(
        "--username",
        type=str,
        help="The Twitter username to build a model for."
    )
    args = parser.parse_args()
    print("Generating model from files: {}".format(args.corpus_dir))
    model = generate_model(args.corpus_dir)
    print("Storing model to {}".format(args.output))
    Writer(args.output).write(model, args.username)
    print("Process complete!")

