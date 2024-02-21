from random import choice

class WordFinder:
    '''Word Finder: finds random words from a text file'''
    def __init__(self, file_path):
        '''Create a list of words from a filepath'''
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



class SpecialWordFinder(WordFinder):
    '''Special Word Finder: finds random words from a text file but ignores comments and whitespace'''
    # Don't need init either, it gets inherited from parent class unless you need to add or
    # remove from the init params
    # def __init__(self, file_path):
    #     '''Create a list of words from a filepath'''
    #     super().__init__(file_path)
    # Python will look for random in the parent if the child doesn't have it. No need to repeat.
    # def random(self):
    #     '''Generates a random word from the self.words list'''

    #     return super().random()

    def get_words(self, file_path):
        '''Opens and reads a file of words and returns a list of them. Filters out
        whitespace, comments and new line characters'''
        # can take from parent
        words_from_parent = super().get_words(file_path)
        # file = open(file_path)

        # word_list = [line.strip() for line in file if line[0] != '#' and bool(line.strip())]
        word_list = [word for word in words_from_parent if word and word[0] != '#']

        return word_list
