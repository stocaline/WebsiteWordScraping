import requests

def countWords(text, word):
    wordCount = text.lower().split().count(word.lower())
    return wordCount

def main():
    url = input("Informe a URL da página: ")
    wordToSearch = input("Informe a palavra para contar: ")

    response = requests.get(url)
    if response.status_code == 200:
        pageContent = response.text

        wordCount = countWords(pageContent, wordToSearch)
        print(f"A palavra '{wordToSearch}' aparece {wordCount} vezes no texto.")

    else:
        print("Não foi possível acessar a página.")

if __name__ == "__main__":
    main()