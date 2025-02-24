import sys

def capitalize_sentence(sentence):
    """Capitalizes the first letter of each sentence."""
    return sentence.capitalize()

if __name__ == "__main__":
    for line in sys.stdin:
        print(capitalize_sentence(line.strip()))