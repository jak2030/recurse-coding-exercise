import argparse
import re

from spacy_markov import SpacyMarkovify

def generate_model(corpus_fpath):
	"""Generate a markov model given a corpus."""
	with open(corpus_fpath) as fh:
		text = fh.read()
		text_model = SpacyMarkovify(text)
		return text_model	

def store_model(model, output_fpath):
	"""Serialize a model to json and write it to a file."""
	model_json = model.to_json()
	with open(output_fpath, "w") as fh:
		fh.write(model_json)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Create a Markov model.")
	parser.add_argument("--corpus", type=str, help="A path to the corpus used for training.")
	parser.add_argument("--output", type=str, help="A path to which to write a serialized version of the model.")
	args = parser.parse_args()
	print("Generating model at {}".format(args.corpus))
	model =	generate_model(args.corpus)
	print("Storing model to {}".format(args.output))
	store_model(model, args.output)
	print("Process complete!")


