import markovify
import spacy

nlp = spacy.load("en")

class SpacyMarkovify(markovify.Text):
    """
    This extends some of the markovify methods for better text parsing.
    This example is from the readme: https://github.com/jsvine/markovify
    """
    def word_split(self, sentence):
        return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence
