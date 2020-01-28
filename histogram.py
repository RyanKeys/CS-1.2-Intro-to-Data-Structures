import sys

source_text = sys.argv[1]


def histogram(source_text):
    source_text = open(source_text)
    source_text = source_text.read().replace("\n", '').split(" ")
    word_frequency = dict()

    for word in source_text:
        word = word.lower()
        if word in word_frequency.keys():
            word_frequency[word] += 1
            pass

        elif word == '':
            pass

        elif word not in word_frequency.keys():
            if "." in word:
                word = word.strip(".")
                word_frequency.update({word: 1})
                pass

            else:
                word_frequency.update({word: 1})g
                pass

        else:
            pass

    return word_frequency


if __name__ == "__main__":
    print(histogram(source_text))
