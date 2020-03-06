from dictogram import Dictogram
from random import randint

class MarkovChain:

    def __init__(self, word_list):


        #The Markov chain will be a dictionary of dictionaries
        #Example: for "one fish two fish red fish blue fish"
        #{"one": {fish:1}, "fish": {"two":1, "red":1, "blue":1}, "two": {"fish":1}, "red": {"fish":1}, "blue": {"fish:1"}}
         self.markov_chain = self.build_markov(word_list)

    def build_markov(self, word_list):
        markov_chain = {}

        for i in range(len(word_list) - 1):
            #get the current word and the word after
            current_word = word_list[i]
            next_word = word_list[i+1]

            if current_word in markov_chain.keys(): #already there
                #get the histogram for that word in the chain
                markov_chain[current_word].add_count(next_word)
                #add to count
            else: #first entry
                markov_chain[current_word] = Dictogram([next_word])

        return markov_chain

    def walk(self, num_words):
        #TODO: generate a sentence num_words long using the markov chain
        start = [list(self.markov_chain.keys())[randint(0,len(self.markov_chain))]]
        for i in range(num_words-1):
            start.append(self.markov_chain[start[-1]].sample())

        return ' '.join(start)


    def print_chain(self):
        for word, histogram in self.markov_chain.items():
            print(word, histogram)



markov_chain = MarkovChain(["one", "fish", "two", "fish", "red", "fish", "blue", "fish"])
sentence = "You don't understand I coulda had class I coulda been a contender I could've been somebody instead of a bum which is what I am"
sentence = sentence.split(" ")
markov_chain.print_chain()
print(markov_chain.walk(10))