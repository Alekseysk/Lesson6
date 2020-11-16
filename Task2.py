"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать
защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного
полотна. Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги
асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.

Например: 20м*5000м*25кг*5см = 12500 т
"""

# Я физик, уж извините, будут делать правильно, а не в килограммах на площадь...

class Road:
    __length: float
    __width: float
    __density: float = 1700  # кг/куб.м
    
    def __init__(self, length: float, width: float):
        self.__length = length
        self.__width = width
    
    def roadbed_mass(self, thickness):
        thickness = thickness / 100  # Толщина в метрах
        volume = self.__length * self.__width * thickness  # В кубометрах
        mass = volume * self.__density  # По объёму и плотности
        return mass


my_way = Road(5000, 20)
print(f'Требуется масса асфальта: {my_way.roadbed_mass(5) / 1000:.2f} тонн')