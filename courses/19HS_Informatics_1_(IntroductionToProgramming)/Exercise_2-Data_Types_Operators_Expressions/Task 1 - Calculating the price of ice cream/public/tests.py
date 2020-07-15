import builtins
import importlib
from unittest import TestCase


def set_vars(price_cone, num_scoops_vanilla, price_per_scoop_vanilla, num_scoops_chocolate, price_per_scoop_chocolate):
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


class PublicTestSuite(TestCase):

    def test_a_simple_order(self):
        set_vars(0.3, 1, 2, 3, 4)
        actual = get_price()
        expected = 14.3

        m = "Calculation not correct for an order with 1 vanilla scoops and 3 chocolate scoops. "
        m += "Prices: cone 0.3CHF, vanilla scoop 2CHF, chocolate scoop 4CHF"
        self.assertAlmostEqual(expected, actual, 5, m)
