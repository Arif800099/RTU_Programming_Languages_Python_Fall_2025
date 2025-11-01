import re

def count_characters(text):
    return len(text.replace(" ", ""))

def count_words(text):
    return len(text.split())

def extract_numbers(text):
    return [int(num) for num in re.findall(r'\d+', text)]

def analyze_text(text):
    chars = count_characters(text)
    words = count_words(text)
    numbers = extract_numbers(text)
    total = sum(numbers) if numbers else 0
    average = total / len(numbers) if numbers else 0
    return chars, words, numbers, total, average

if __name__ == "__main__":
    text = input("Enter text: ")
    chars, words, numbers, total, average = analyze_text(text)
    print(f"Non-space characters: {chars}")
    print(f"Word count: {words}")
    print(f"Numbers found: {numbers}")
    print(f"Sum of numbers: {total}")
    print(f"Average of numbers: {average:.2f}")
