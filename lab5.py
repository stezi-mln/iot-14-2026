from enum import Enum

class Type(Enum):
    TERRESTRIAL = 0 #земні
    JOVIAN = 1      #газові

class Planet:
    def __init__(self, name, mass_in_kg, orbital_velocity, mean_temperature, len_of_day, dist_from_sun, planet_type):
        self.__name = name
        self.__mass_in_kg = mass_in_kg
        self.__orbital_velocity = orbital_velocity
        self.__mean_temperature = mean_temperature
        self.__len_of_day = len_of_day
        self.__dist_from_sun = dist_from_sun
        self.type = planet_type

    def display_info(self):
        print(f"------ Інформація про планету {self.__name} ------\nНазва: {self.__name}\nМаса в кг: {self.__mass_in_kg}\nОрбітальна швидкість:{self.__orbital_velocity}\nСередня температура: {self.__mean_temperature}\nДовжина дня: {self.__len_of_day}\nВідстань від сонця:{self.__dist_from_sun}\nТип планети: {self.type.name}\n{"-" * 30}\n ")

    def __del__(self):
        print(f"Планету {self.__name} видалено")

    def get_name(self):
        return self.__name

    def get_mass_in_kg(self):
        return self.__mass_in_kg

    def get_orbital_velocity(self):
        return self.__orbital_velocity

    def get_mean_temperature(self):
        return self.__mean_temperature

    def get_len_of_day(self):
        return self.__len_of_day

    def get_distance_from_sun(self):
        return self.__dist_from_sun

class Planetary:
    def __init__(self, name):
        self.planets = []
        self.name = name

    def add_planet(self, planet):
        self.planets.append(planet)

    def sort_by_len_of_day(self):
        self.planets.sort(key = lambda planet: planet.get_len_of_day())
        for planet in self.planets:
            print(planet.get_name(), '-', planet.get_len_of_day())

def findDistanceBetweenPlanet(planetA, planetB):
    return f"Відстань від планети {planetA.get_name()} до планети {planetB.get_name()} становить {abs(planetA.get_distance_from_sun() - planetB.get_distance_from_sun())}\n{"_" * 92}"

def findAverageMass(planetary):
    total_mass = 0
    for planet in planetary.planets:
        total_mass += planet.get_mass_in_kg()
    average_mass = total_mass / len(planetary.planets) if planetary.planets else 0
    print(f" \nСередня маса планетарію {planetary.name} становить {average_mass}\n{"_" * 92}")


def main():
    earth = Planet("Земля", 5.972e24, 29.78, 15, 24, 149.6, Type.TERRESTRIAL)
    mars = Planet("Марс", 6.39e23, 24.07, -65, 24.6, 227.9, Type.TERRESTRIAL)
    jupiter = Planet("Юпітер", 1.898e27, 13.07, -110, 9.9, 778.5, Type.JOVIAN)
    saturn = Planet("Сатурн", 5.683e26, 9.69, -140, 10.7, 1433.5, Type.JOVIAN)

    my_planets = Planetary('мої улюблені планети')
    my_planets.add_planet(earth)
    my_planets.add_planet(mars)
    my_planets.add_planet(jupiter)
    my_planets.add_planet(saturn)


    earth.display_info()
    mars.display_info()
    jupiter.display_info()
    saturn.display_info()
    my_planets.sort_by_len_of_day()
    findAverageMass(my_planets)
    findDistanceBetweenPlanet(earth, mars)



main()