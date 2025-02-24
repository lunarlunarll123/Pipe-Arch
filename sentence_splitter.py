import sys
import re

def split_sentences(text):
    """Splits text into sentences using punctuation."""
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return sentences

if __name__ == "__main__":
    for line in sys.stdin:
        sentences = split_sentences(line)
        for sentence in sentences:
            print(sentence)