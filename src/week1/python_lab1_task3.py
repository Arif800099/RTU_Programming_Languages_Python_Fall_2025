def analyze_sentence(text):
    length = len(text)
    words = len(text.split())
    contains_python = "python" in text.lower()
    return length, words, contains_python

if __name__ == "__main__":
    text = input("Enter a sentence: ")
    length, words, contains_python = analyze_sentence(text)
    print(f"Total characters: {length}")
    print(f"Word count: {words}")
    print(f"Contains 'Python': {contains_python}")
