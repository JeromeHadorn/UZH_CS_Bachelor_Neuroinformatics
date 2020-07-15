from random import choice, shuffle
from game_logic import GameLogic
# This is the current version of WordLogic that needs to be adapted
class WordLogic(GameLogic):

    def __init__(self, num_words, len_words, num_attempts):
        GameLogic.__init__(self,num_words,len_words,num_attempts)

    def _word_selection(self):
        words = self._find_words_with_right_size()
        shuffle(words)
        return words[0:self.num_words]

    def _find_words_with_right_size(self):
        with open("../resource/words.txt") as f:
            word_list = f.read().splitlines()
            print(word_list)
        return [word.upper() for word in word_list if len(word) is self.len_words]
    def check(self, guess):
        if len(guess) != self.len_words:
            return False, ["Wrong length"]
        else:
            return super().check(guess)
