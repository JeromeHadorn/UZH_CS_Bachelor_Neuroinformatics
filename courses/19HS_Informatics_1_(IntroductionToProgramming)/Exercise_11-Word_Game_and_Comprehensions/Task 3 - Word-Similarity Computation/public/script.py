import random
import math
import difflib

class WordLogic(object):

    def __init__(self, num_words, len_words):
        self.num_words = num_words
        self.len_words = len_words

    def find_words_with_right_size(self):
        with open("../resource/words.txt") as f:
            word_list = f.read().splitlines()
        return [word.upper() for word in word_list if len(word) is self.len_words]

    def word_selection(self):
        words = self.find_words_with_right_size()
        i = math.floor(len(words)/3)
        random.shuffle(words)
        words[0:i]

        output = []
        randomPick = random.choice(words)
        words.remove(randomPick)

        while len(output) < self.num_words:


            if self.is_similar(randomPick,words[0],0.4):
                output.append(words[0])
                print(randomPick, words[0])
            words.pop(0)


        return output

    def is_similar(self, a, b, threshold):
        ratio = difflib.SequenceMatcher(None, a, b).ratio()
        if ratio > threshold:
            return True
        else:
            return False

w = WordLogic(10,7)
print(w.word_selection())

print(difflib.SequenceMatcher(None, 'tide', 'diet').ratio())
