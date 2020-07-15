from unittest import TestCase
from car import Car
from combustion_car import CombustionCar
from electric_car import ElectricCar
from hybrid_car import HybridCar


class TestCars(TestCase):

    def test_abstract(self):
        with self.assertRaises(TypeError):
            car = Car()

    def test_comb_remaining_range(self):
        c = CombustionCar(40.0, 8.0)
        self.assertAlmostEqual(500.0, c.get_remaining_range(), delta=0.001)

    def test_comb_drive(self):
        c = CombustionCar(40.0, 8.0)
        c.drive(25.0)
        self.assertAlmostEqual(38.0, c.get_gas_tank_status()[0], delta=0.001)

    def test_comb_state(self):
        c = CombustionCar(40.0, 8.0)
        c.drive(25.0)
        self.assertEqual((38.0, 40.0), c.get_gas_tank_status())

    def test_comb_overfill(self):
        c = CombustionCar(40.0, 8.0)
        with self.assertRaises(Warning):
            c.fuel(1)

    def test_comb_nofuel(self):
        c = CombustionCar(40.0, 8.0)
        with self.assertRaises(Warning):
            c.drive(501)

    def test_elec_remaining_range(self):
        c = ElectricCar(40.0, 500.0)
        self.assertAlmostEqual(500.0, c.get_remaining_range(), delta=0.001)

    def test_elec_drive(self):
        c = ElectricCar(40.0, 500.0)
        c.drive(25.0)
        self.assertAlmostEqual(38.0, c.get_battery_status()[0], delta=0.001)

    def test_elec_state(self):
        c = ElectricCar(40.0, 500.0)
        c.drive(25.0)
        self.assertEqual((38.0, 40.0), c.get_battery_status())

    def test_elec_overfill(self):
        c = ElectricCar(40.0, 500.0)
        with self.assertRaises(Warning):
            c.charge(1)

    def test_elec_nofuel(self):
        c = ElectricCar(40.0, 500.0)
        with self.assertRaises(Warning):
            c.drive(501)

    def test_hybr_remaining_range(self):
        c = HybridCar(40.0, 8.0, 40.0, 500.0)
        self.assertAlmostEqual(1000.0, c.get_remaining_range(), delta=0.001)

    def test_hybr_drive(self):
        c = HybridCar(40.0, 8.0, 40.0, 500.0)
        c.drive(25.0)
        self.assertAlmostEqual(38.0, c.get_battery_status()[0], delta=0.001)

    def test_hybr_state(self):
        c = HybridCar(40.0, 8.0, 40.0, 500.0)
        c.drive(25.0)
        self.assertEqual((38.0, 40.0), c.get_battery_status())

    def test_hybr_overfill(self):
        c = HybridCar(40.0, 8.0, 40.0, 500.0)
        with self.assertRaises(Warning):
            c.fuel(1)

    def test_hybr_nofuel(self):
        c = HybridCar(40.0, 8.0, 40.0, 500.0)
        with self.assertRaises(Warning):
            c.drive(1001)

    def test_autoswitch1(self):
        h = HybridCar(40.0, 8.0, 40.0, 500.0)
        h.switch_to_combustion()
        h.drive(600.0)  # depletes fuel, auto-switch
        self.assertEqual(h.get_gas_tank_status(), (0.0, 40.0))

    def test_autoswitch2(self):
        h = HybridCar(40.0, 8.0, 40.0, 500.0)
        h.switch_to_combustion()
        h.drive(600.0)  # depletes fuel, auto-switch
        self.assertEqual(h.get_battery_status(), (32.0, 40.0))

    def test_autoswitch3(self):
        h = HybridCar(40.0, 8.0, 40.0, 500.0)
        h.drive(600.0)  # depletes fuel, auto-switch
        self.assertEqual(h.get_battery_status(), (0.0, 40.0))

    def test_autoswitch4(self):
        h = HybridCar(40.0, 8.0, 40.0, 500.0)
        h.drive(600.0)  # depletes fuel, auto-switch
        self.assertEqual(h.get_gas_tank_status(), (32.0, 40.0))

    def test_handle1(self):
        with self.assertRaises(Warning):
            h = HybridCar(40.0, 'x', 40.0, 500.0)

    # This current test suite only contains very basic test cases. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
