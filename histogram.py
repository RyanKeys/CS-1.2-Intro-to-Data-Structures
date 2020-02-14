import sys      
import random
from cleanup import cleanup
source_text = sys.argv[1]


class Dictogram:
    def __init__(self):
        self.source_text = source_text

    def histogram(self, source_text):
        '''Takes source text and counts frequency of each word used. Returns Dict()'''
        source_text = cleanup(source_text)
        word_frequency = dict()

        for word in source_text:
            # Adds to word if it's already in the dictionary
            if word in word_frequency.keys():
                word_frequency[word] += 1
                pass

            elif word == '':
                pass

            elif word not in word_frequency.keys():
                # Removes periods from word then adds it to dict
                if "." in word:
                    word = word.strip(".")
                    word_frequency.update({word: 1})
                    pass
                
                # Adds word to dict
                else:
                    word_frequency.update({word: 1})
                    pass

            else:
                pass

        return word_frequency


    def weighted_histogram(source_text):
        '''Takes source text and returns dict as percentages values'''
        word_frequency = histogram(source_text)
        weighted_histo = {}
        total_items = len(word_frequency.values())

        for key, value in word_frequency.items():
            value = value / total_items
            weighted_histo.update({f"{key}": float(f"{value}")})
            
        return weighted_histo


    def histogram_randomizer(source_text):
        '''Randomly creates a sentence from source text'''
        words = []
        random_sentence = []

        for word in histogram(source_text):
            words.append(word)
            rando_word = random.choice(words)
            random_sentence.append(rando_word)

        # returns random sentence as a str
        return ' '.join(random_sentence) + "."

class Listogram:
    def __init__(self):
        self.source_text = source_text


    def list_histogram(self, source_text):
        '''Takes source text and returns frequency of each word used in a list'''
        source_text = cleanup(source_text)
        listo = []
        words = []
        for word in source_text:
            if word in listo:
                count = source_text.count(word)
                listo.insert(listo.index(word)+1, [word, count])
                words.append(word)
                listo.pop(listo.index(word))

            elif word in words:
                pass

            elif word not in listo:
                listo.append(word)
        return listo


if __name__ == "__main__":
    d = Dictogram()
    l = Listogram()
    print(d.histogram(source_text))
    print(l.list_histogram(source_text))