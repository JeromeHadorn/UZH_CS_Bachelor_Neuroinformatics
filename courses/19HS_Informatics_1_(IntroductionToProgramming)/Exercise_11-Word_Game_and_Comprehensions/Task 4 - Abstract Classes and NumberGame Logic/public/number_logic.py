from random import choice, shuffle, random, randint
from game_logic import GameLogic
# This is the current version of WordLogic that needs to be adapted
class NumberLogic(GameLogic):

    def __init__(self, num_words, len_words, num_attempts):
        GameLogic.__init__(self,num_words,len_words,num_attempts)

    def _word_selection(self):
        allNumbers = []


        while len(allNumbers) < self.num_words:
            numbers = []
            while len(numbers) < self.len_words:
                guess = randint(1,9)

                if not guess in numbers:
                    numbers.append(guess)

            number = 0
            for i,val in enumerate(numbers):
                number += (val * (10 ** (len(numbers) - i -1)))
            print(number)
            allNumbers.append(number)

        print("allnumbers", allNumbers)
        return allNumbers

        #return [1234]

    def check(self,guess):

        if self._containsmultiplenumbers(guess) == False:
            raise Warning()
        else:
            return super().check(guess)

    def _find_words_with_right_size(self):
        pass

    def _containsmultiplenumbers(self,number):
        dict = {}

        for num in str(number):
            if num in dict:
                dict[num] += 1
                print(dict)
                return False
            else:
                dict[num] = 1


        return  True

    def _generate_feedback(self, guess):
        num = str(guess)
        matching = 0
        for n in num:
            if n in str(self.password):
                matching += 1
        return "%d/%d correct" % (matching, self.len_words)