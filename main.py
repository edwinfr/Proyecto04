from word_counter import count_words


if __name__ == "__main__":
    text = input("Ingresa un texto: ")
    print(f"Número de palabras: {count_words(text)}")
