# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.


class Cell:
    def __init__(self, quan_c):
        self.quan_c = quan_c        # количество клеток quantity cell

    def __add__(self, other):
        return self.quan_c + other

    def __sub__(self, other):
        return self.quan_c - other

    def __mul__(self, other):
        return self.quan_c * other

    def __truediv__(self, other):
        return round(self.quan_c / other)

    def make_cell(self, cell_in_row):       # количество клеток в ряду
        self.cell_fall = ""
        while self.quan_c > 0:
            self.quan_c -= cell_in_row
            if self.quan_c < 0:
                self.cell_fall += ("*" * (cell_in_row + self.quan_c) + "\n")
            else:
                self.cell_fall += ("*" * cell_in_row + "\n")
        return self.cell_fall

    def __call__(self, new_quan_c):
        self.quan_c = new_quan_c


c = Cell(52)                # введите количество клеток
print(c.make_cell(10))      # количество клеток в ряду
print(c+15)
c(99)
print(c.quan_c)
print(c/2)
