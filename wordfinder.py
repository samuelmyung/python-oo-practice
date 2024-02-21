class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, file_path):
        # call another function to generate words
        self.words = self.get_words(file_path)



    def random(self):
        ''' Generates a random word from the self.words list '''
        pass

    def get_words(self, file_path):
        ''' Opens and reads a file of words and returns a list of them'''
        file = open(file_path)

        word_list = [line[0:-2] for line in file]

        file.close()

        return word_list


