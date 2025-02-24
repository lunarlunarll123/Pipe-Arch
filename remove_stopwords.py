import sys

STOPWORDS = {"the", "is", "in", "at", "which", "on", "and", "a", "an", "to", "of", "that", "this"}

def remove_stopwords(sentence):
    """Removes common stopwords from a sentence."""
    words = sentence.split()
    filtered_words = [word for word in words if word.lower() not in STOPWORDS]
    return " ".join(filtered_words)

if __name__ == "__main__":
    for line in sys.stdin:
        cleaned_sentence = remove_stopwords(line.strip())
        print(cleaned_sentence)