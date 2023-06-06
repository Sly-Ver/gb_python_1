# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т


# class Road:
#     def __init__(self, length: int, width: int):
#         self._length = length
#         self._width = width
#
#     def get_mass(self, mass_1m2: int, thickness: int) -> int:
#         """
#         Расчет массы асфальта
#         :param mass_1m2: масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см
#         :param thickness: толщины полотна
#         :return: масса асфальта в тоннах
#         """
#         mass = self._length * self._width * mass_1m2 * thickness // 1000
#         return mass
#
#
# road = Road(5000, 20)
# assert road.get_mass(25, 5) == 12500


class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width, weight, depth):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.depth = depth

    def mass(self):
        leng = self._length
        wid = self._width
        w = self.weight
        dep = self.depth
        total = leng * wid * w * dep / 1000
        return print(f"Масса асфальта\n {leng} м * {wid} м * {w} кг * {dep} см = ", total, "т")


r = Road(25, 5000, 25, 5)
r.mass()