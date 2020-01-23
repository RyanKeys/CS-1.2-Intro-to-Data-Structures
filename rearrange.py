import random


def rearrange(sentence):
    words = sentence.split(" ")
    for word in words:
        random.shuffle(words)

    return ' '.join(words)


if __name__ == "__main__":
    print(rearrange(sentence))
