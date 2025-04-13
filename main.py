import requests
from collections import Counter

def get_text(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def count_words_in_text(text, words_to_count):
    text_lower = text.lower()
    tokens = text_lower.split()
    counter = Counter(tokens)

    frequencies = {}
    for word in words_to_count:
        w_lower = word.lower()
        frequencies[word] = counter[w_lower]

    return frequencies

def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"
    
    with open(words_file, 'r', encoding='utf-8') as file:
        words_to_count = [line.strip() for line in file if line.strip()]

    text = get_text(url)
    frequencies = count_words_in_text(text, words_to_count)
    print(frequencies)

if __name__ == "__main__":
    main()
