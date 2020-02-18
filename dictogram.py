import random

class Dictogram:

    def __init__(self, word_list):
        '''Initializes the dictogram properties'''

        self.word_list = word_list
       
        self.dictionary_histogram = self.build_dictogram()

        self.tokens = sum(self.dictionary_histogram.values())
        self.types = self.unique_words()

    def build_dictogram(self): 
        '''Creates a histogram dictionary using the word_list property and returns it'''

        #TODO: use your histogram function as a starting point to complete this method
        word_frequency = {}

        for word in self.word_list:
            if word in word_frequency.keys():
                word_frequency[word] += 1
                pass

            elif word not in word_frequency:
                word_frequency.update({word: 1})

            else:
                pass
        return word_frequency

    

    def frequency(self, word):
        '''returns the frequency or count of the given word in the dictionary histogram'''
        #TODO: use your frequency function as a starting point to complete this method
        print(word)
        dicto = self.dictionary_histogram
        print(dicto)
        print(dicto.get(word))
        return dicto.get(word)
            
            

    def unique_words(self):
        '''returns the number of unique words in the dictionary histogram'''
        #TODO: use your unique words function as a starting point to complete this method
        word_list = []
        dicto = self.dictionary_histogram

        for word in dicto:
            if word not in word_list:
                word_list.append(word)

            elif word in word_list:
                pass

        return len(word_list)
           

    def sample(self):
        '''Randomly samples from the dictionary histogram based on the frequency, returns a word'''

        #TODO: use your sample function as a starting point to complete this method
        word_list = []
        dicto = self.dictionary_histogram

        for word in dicto:
            word_list.append(word)
            num = dicto.get(word)
            num = num/len(dicto)

        first_word = word_list[random.randint(1,len(word_list)-1)]
        second_word = word_list[random.randint(1,len(word_list)-1)]
        first_value = dicto.get(first_word)
        second_value = dicto.get(second_word)

        if first_value > second_value:
            return first_value
            

        elif first_value < second_value:
            return second_value
        
        elif first_value == second_value:
            coin_toss = random.choice(word_list)
            return dicto.get(coin_toss)


        
    
def print_dictogram(word_list):
    '''Creates a dictionary based histogram (dictogram) and then prints out its properties and samples from it'''

    print()
    print('Dictionary Histogram:')
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    dictogram = Dictogram(word_list)
    print('dictogram: {}'.format(dictogram.dictionary_histogram))
    print('{} tokens, {} types'.format(dictogram.tokens, dictogram.types))
    for word in word_list[-2:]:
        freq = dictogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    print_dictogram_samples(dictogram)

def print_dictogram_samples(dictogram):
    '''Compares sampled frequency to observed frequency'''

    print('Dictionary Histogram samples:')
    # Sample the histogram 10,000 times and count frequency of results
    samples_list = [dictogram.sample() for _ in range(10000)]
    samples_hist = Dictogram(samples_list)
    print('samples: {}'.format(samples_hist.dictionary_histogram))
    print()
    print('Sampled frequency and error from observed frequency:')
    header = '| word type | observed freq | sampled freq  |  error  |'
    divider = '-' * len(header)
    print(divider)
    print(header)
    print(divider)
    # Colors for error
    green = '\033[32m'
    yellow = '\033[33m'
    red = '\033[31m'
    reset = '\033[m'
    # Check each word in original histogram
    for word, count in dictogram.dictionary_histogram.items():
        # Calculate word's observed frequency
        observed_freq = count / dictogram.tokens
        # Calculate word's sampled frequency
        samples = samples_hist.frequency(word)

        sampled_freq = samples / samples_hist.tokens
        # Calculate error between word's sampled and observed frequency
        error = (sampled_freq - observed_freq) / observed_freq
        color = green if abs(error) < 0.05 else yellow if abs(error) < 0.1 else red
        print('| {!r:<9} '.format(word)
            + '| {:>4} = {:>6.2%} '.format(count, observed_freq)
            + '| {:>4} = {:>6.2%} '.format(samples, sampled_freq)
            + '| {}{:>+7.2%}{} |'.format(color, error, reset))
    print(divider)
    print()

def test():
    d = Dictogram(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])
    print(d.build_dictogram())
    print(d.frequency("fish"))
    print(d.unique_words())
    print(d.sample())

#print_dictogram(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])

if __name__ == "__main__":
    test()
    pass