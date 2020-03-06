import random

class Dictogram(dict):

    def __init__(self, word_list=None):
        '''Initializes the dictogram properties'''
        self.word_list = word_list
        super(Dictogram, self).__init__()
        self.types = 0
        self.tokens = 0
        if word_list is not None:
            for word in word_list:
                self.add_count(word)


    def add_count(self, word, count=1):
        if word in self:
            self[word] += count
        else:
            self[word] = count
        self.types = len(self)
        self.tokens += count 


    def frequency(self, word):
        '''returns the frequency or count of the given word in the dictionary histogram'''
        #TODO: use your frequency function as a starting point to complete this method
        if word in self:
            return self[word]
        else:
            return 0
           

    def sample(self):
        '''Randomly samples from the dictionary histogram based on the frequency, returns a word'''

        #TODO: use your sample function as a starting point to complete this method
        selection = random.random()
        percents = [0]
        for word, count in self.items():
            percents.append((count / self.tokens) + percents[-1])
            if percents[-2] <= selection < percents[-1]:
                return word
    
def print_histogram(word_list):
    print()
    print('Histogram:')
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Dictogram(word_list)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    print_histogram_samples(histogram)


def print_histogram_samples(histogram):
    print('Histogram samples:')
    # Sample the histogram 10,000 times and count frequency of results
    samples_list = [histogram.sample() for _ in range(10000)]
    samples_hist = Dictogram(samples_list)
    print('samples: {}'.format(samples_hist))
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
    for word, count in histogram.items():
        # Calculate word's observed frequency
        observed_freq = count / histogram.tokens
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

word_list = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
def test():
    d = Dictogram(word_list)


if __name__ == "__main__":
    print_histogram(word_list)

    test()
    pass