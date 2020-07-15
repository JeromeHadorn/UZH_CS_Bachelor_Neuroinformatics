import builtins
import importlib
from unittest import TestCase


def set_vars(price_cone, num_scoops_vanilla, price_per_scoop_vanilla, num_scoops_chocolate, price_per_scoop_chocolate):
    try: del script.price_cone
    except: pass
    try: del script.price_per_scoop_vanilla
    except: pass
    try: del script.price_per_scoop_chocolate
    except: pass
    try: del script.num_scoops_vanilla
    except: pass
    try: del script.num_scoops_chocolate
    except: pass

    builtins.price_cone = price_cone
    builtins.price_per_scoop_vanilla = price_per_scoop_vanilla
    builtins.price_per_scoop_chocolate = price_per_scoop_chocolate
    builtins.num_scoops_vanilla = num_scoops_vanilla
    builtins.num_scoops_chocolate = num_scoops_chocolate


set_vars(0,0,0,0,0)
from public import script


def get_price():
    importlib.reload(script)
    return script.price


class PrivateTestSuite(TestCase):

    def _test(self, price_cone, num_scoops_vanilla, price_per_scoop_vanilla, num_scoops_chocolate, price_per_scoop_chocolate, expected):
        set_vars(price_cone, num_scoops_vanilla, price_per_scoop_vanilla, num_scoops_chocolate, price_per_scoop_chocolate)
        actual = get_price()

        m = "@@Calculation not correct for an order with {} vanilla scoops and {} chocolate scoops. "
        m += "Prices: cone {}CHF, vanilla scoop {}CHF, chocolate scoop {}CHF@@"
        m = m.format(num_scoops_vanilla, num_scoops_chocolate, price_cone, price_per_scoop_vanilla, price_per_scoop_chocolate)
        self.assertAlmostEqual(expected, actual, 5, m)

    def test_no_ice_cream(self):
        self._test(0.1, 0, 1, 0, 2, 0.1)

    def test_free_ice_cream(self):
        self._test(0.2, 10, 0, 20, 0, 0.2)

    def test_a_simple_order(self):
        self._test(0.3, 1, 2, 3, 4, 14.3)

    def test_another_simple_order(self):
        self._test(0.4, 2, 3, 4, 5, 26.4)

    def test_only_vanilla(self):
        self._test(0.5, 2, 1.23, 0, 2.34, 2.96)

    def test_only_choc(self):
        self._test(0.6, 0, 3.45, 2, 4.56, 9.72)
