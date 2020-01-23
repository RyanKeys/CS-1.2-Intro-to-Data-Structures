import random


def rearrange(sentence):
    words = sentence.split(" ")
    for word in words:
        random.shuffle(words)

    return ' '.join(words)


def reverse_sentence(sentence):
    return " ".join(sentence.split(" ")[::-1])


def reverse_words(sentence):
    word_list = []
    words = sentence.split(" ")
    for word in words:
        word = word[::-1]
        word_list.append(word)
    output = " ".join(word_list)
    return output


if __name__ == "__main__":
    sentence = "how now brown cow"
    print(rearrange(sentence))
    print(reverse_sentence(sentence))
    print(reverse_words(sentence))
