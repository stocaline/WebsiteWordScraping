import re
import requests
from bs4 import BeautifulSoup


def clear_list(list_of_words):
    clean_list = []
    for item in list_of_words:
        if item.strip():
            clean_list.append(item)
    return clean_list


def count_word(text, word):
    word_count = text.lower().split().count(word.lower())
    return word_count


def word_average_per_sentence(words):
    sentences = re.split(r'[.!?|-]', words)
    amount_sentences = len(sentences)
    amount_words = 0

    for sentence in sentences:
        words = sentence.split(" ")
        words = clear_list(words)
        if len(words) > 1:
            amount_words += len(words)

    if amount_sentences > 0:
        word_average = amount_words / amount_sentences
        return round(word_average, 2)
    else:
        return 0


def unique_words(words):
    sentences = re.split(r'[.!?|-]', words)
    words_list = []
    unique_words_list = []
    word_counter = {}

    for sentence in sentences:
        words = sentence.split(" ")
        words = clear_list(words)
        if len(words) > 1:
            words_list.extend(words)

    for word in words_list:
        word_counter[word] = word_counter.get(word, 0) + 1

    for word, amount in word_counter.items():
        if amount == 1:
            unique_words_list.append(word)

    return unique_words_list


def main():
    url = input("Informe a URL da página: ")
    word_to_search = input("Informe a palavra para contar: ")

    response = requests.get(url)
    if response.status_code == 200:
        page_content = BeautifulSoup(response.text, 'html.parser')
        text = ' '.join(page_content.stripped_strings)

        # word_average_per_sentence(text)
        amount_words = count_word(text, word_to_search)
        average_words = word_average_per_sentence(text)
        unique_words_list = unique_words(text)

        print(f"A palavra '{word_to_search}' aparece {amount_words} vezes no texto.")
        print(f"A média de palavras por frase é de {average_words}")
        print(f"As palavras unicas no texto são {unique_words_list}")
    else:
        print("Não foi possível acessar a página.")


if __name__ == "__main__":
    main()
