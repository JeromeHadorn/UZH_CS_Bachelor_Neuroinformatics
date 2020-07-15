# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from car import Car

class ElectricCar(Car):

    def __init__(self, battery_size, battery_range_km):
        if isinstance(battery_size, float) and battery_size >= 0 and isinstance(battery_range_km,float) and battery_range_km >= 0:
            self.__battery_size = self.__current = battery_size
            self.__battery_per_100km = 100 * battery_size / battery_range_km
        else:
            raise Warning

    def charge(self, kwh):
        if isinstance(kwh, float) and kwh >= 0:
            if self.__current + kwh <= self.__battery_size:
                self.__current += kwh
            else:
                raise Warning
        else:
            raise Warning

    def get_battery_status(self):
        return (self.__current, self.__battery_size)

    def get_remaining_range(self):
        return self.__current / (self.__battery_per_100km / 100)

    def drive(self, dist):
        if isinstance(dist, float) and dist >= 0:
            if self.__current - (self.__battery_per_100km / 100) * dist <= 0:
                self.__current = 0.0
                raise Warning
            else:
                self.__current -= (self.__battery_per_100km / 100) * dist
        else:
            raise Warning