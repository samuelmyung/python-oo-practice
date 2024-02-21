from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, file_path):
        '''Create a list of words from a text file'''
        self.words = self.get_words(file_path)

    def random(self):
        '''Generates a random word from the self.words list'''
        return choice(self.words)

    def get_words(self, file_path):
        '''Opens and reads a file of words, splitting on new lines, and returns a list of them'''
        file = open(file_path)

        word_list = [line.strip() for line in file]

        file.close()

        return word_list


