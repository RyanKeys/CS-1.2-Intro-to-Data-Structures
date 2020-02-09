def cleanup(source_text):
    source_text = open(source_text)
    source_text = source_text.read().replace("\n", " ").split(" ")
    for word in source_text:
        word = word.lower()
    return source_text


if __name__ == "__main__":
    print(cleanup("test.txt"))