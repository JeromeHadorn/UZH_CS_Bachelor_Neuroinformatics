import random

class GameRunner(object):

    def __init__(self):
        self.rows = 17
        self.columns = 2

    def generate_hex_codes(self):
        randomString = "0123456789ABCDEF"
        codes = []
        for i in range(self.columns * self.rows):
            codes.append("0x" + "".join([ random.choice(randomString) for r in range(4)]))
        return codes


g = GameRunner()
g.generate_hex_codes()