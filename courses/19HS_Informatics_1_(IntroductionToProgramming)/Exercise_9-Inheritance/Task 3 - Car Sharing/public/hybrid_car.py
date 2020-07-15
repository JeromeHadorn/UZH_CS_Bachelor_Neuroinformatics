# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from combustion_car import CombustionCar
from electric_car import ElectricCar

class HybridCar(CombustionCar, ElectricCar):

        def __init__(self, gas_capacity, gas_per_100km, battery_size, battery_range_km):
            ElectricCar.__init__(self, battery_size, battery_range_km)
            CombustionCar.__init__(self, gas_capacity, gas_per_100km)
            self.__mode = 'e'

        def switch_to_combustion(self):
            self.__mode = 'c'

        def switch_to_electric(self):
            self.__mode = 'e'

        def get_remaining_range(self):
            return CombustionCar.get_remaining_range(self) + ElectricCar.get_remaining_range(self)

        def drive(self, dist):
            if not isinstance(dist, float):
                raise Warning
            if self.__mode == 'c':
                try:
                    driven_distance = CombustionCar.get_remaining_range(self)
                    CombustionCar.drive(self, dist)
                except Warning:
                    dist -= driven_distance
                    self.switch_to_electric()
                    ElectricCar.drive(self, dist)

            elif self.__mode == 'e':
                try:
                    driven_distance = ElectricCar.get_remaining_range(self)
                    ElectricCar.drive(self, dist)
                except Warning:
                    dist -= driven_distance
                    self.switch_to_combustion()
                    CombustionCar.drive(self, dist)
