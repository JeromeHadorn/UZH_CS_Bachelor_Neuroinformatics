from random import choice, shuffle
from abc import ABC, abstractmethod
# This is the current version of WordLogic that needs to be adapted
class GameLogic(ABC):

    def __init__(self, num_words, len_words, num_attempts):
        self.num_words = num_words
        self.len_words = len_words
        self.num_attempts = num_attempts
        self.words = self._word_selection()
        self.password = choice(self.words)

    @ abstractmethod
    def _word_selection(self):
        pass

    @ abstractmethod
    def _find_words_with_right_size(self):
        pass

    def check(self, guess):
        if self.num_attempts == 0:
            raise Warning("No attempts left")
        # if len(guess) != self.len_words:
        #     return False, ["Wrong length"]
        if guess == self.password:
            return True, ["Access granted!"]
        else:
            self.num_attempts -= 1
            return False, [
                self._generate_feedback(guess),
                "Access denied!"
            ]

    def _generate_feedback(self, guess):
        matching = 0
        for i in range(self.len_words):
            if guess[i] == self.password[i]: matching += 1
        self.num_attempts = self.num_attempts - 1
        return "%d/%d correct" % (matching, self.len_words)
