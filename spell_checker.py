import sys
from textblob import TextBlob

def correct_spelling(sentence):
    """Uses TextBlob to correct spelling mistakes in a sentence."""
    return str(TextBlob(sentence).correct())

if __name__ == "__main__":
    for line in sys.stdin:
        corrected_sentence = correct_spelling(line.strip())
        print(corrected_sentence)