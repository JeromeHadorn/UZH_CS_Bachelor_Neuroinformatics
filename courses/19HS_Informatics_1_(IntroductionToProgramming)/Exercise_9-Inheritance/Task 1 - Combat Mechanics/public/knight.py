# Implement this class. Extend Character and adopt the combat
# mechanics that are defined in the description. Do not change the
# class name and stick to the method signatures of Character
# or the automated grading won't work.

from character import Character

class Knight(Character):
    def __init__(self, name, lvl):
        super().__init__(name,lvl)

    def _take_physical_damage(self, amount):
        assert isinstance(amount, int)
        assert amount >= 0
        self._health_cur = max(0, self._health_cur - (amount * 0.75))

    def _get_caused_dmg(self, other):
        return round(0.8 * max(1, self._lvl * 11 - other._lvl))