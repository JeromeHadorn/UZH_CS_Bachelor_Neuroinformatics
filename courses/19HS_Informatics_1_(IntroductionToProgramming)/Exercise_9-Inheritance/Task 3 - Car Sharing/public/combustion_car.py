# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from car import Car

class CombustionCar(Car):

    def __init__(self, gas_capacity, gas_per_100km):
        if isinstance(gas_capacity, float) and gas_capacity >= 0 and isinstance(gas_per_100km, float) and gas_per_100km >= 0:
            self.__gas_capacity = self.__current_gas = gas_capacity
            self.__gas_per_100km = gas_per_100km
        else:
            raise Warning

    def fuel(self, f):
        if isinstance(f, float) and f >= 0:
            if self.__current_gas + f <= self.__gas_capacity:
                self.__current_gas += f
            else:
                raise Warning
        else:
            raise Warning

    def get_gas_tank_status(self):
        return (self.__current_gas, self.__gas_capacity)

    def get_remaining_range(self):
        return 100 * self.__current_gas / self.__gas_per_100km

    def drive(self, dist):
        if isinstance(dist, float) and dist >= 0:
            if self.__current_gas - (self.__gas_per_100km / 100) * dist <= 0:
                self.__current_gas = 0.0
                raise Warning
            else:
                self.__current_gas -= (self.__gas_per_100km / 100) * dist
        else:
            raise Warning
