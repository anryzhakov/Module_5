# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Домашняя работа по уроку "Перегрузка операторов."

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, House)):
            raise TypeError("Операнд справа должен иметь тип int или House")
        return other if isinstance(other, int) else other.number_of_floors

    @classmethod
    def __verify_val(cls, value):
        if not isinstance(value, (int, House)):
            raise ArithmeticError("Правый операнд должен быть типом int или объектом House")
        return value if isinstance(value, int) else value.number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

    def __eq__(self, other):
        _other = self.__verify_data(other)
        return self.number_of_floors == _other

    def __lt__(self, other):
        _other = self.__verify_data(other)
        return self.number_of_floors < _other

    def __le__(self, other):
        _other = self.__verify_data(other)
        return self.number_of_floors <= _other

    def __gt__(self, other):
        _other = self.__verify_data(other)
        return self.number_of_floors > _other

    def __ge__(self, other):
        _other = self.__verify_data(other)
        return self.number_of_floors >= _other

    def __ne__(self, other):
        _other = self.__verify_data(other)
        return self.number_of_floors != _other

    def __add__(self, value):
        _value = self.__verify_val(value)
        self.number_of_floors = self.number_of_floors + _value
        return self

    def __radd__(self, value):
        _value = self.__verify_val(value)
        self.number_of_floors = _value + self.number_of_floors
        return self

    def __iadd__(self, value):
        _value = self.__verify_val(value)
        self.number_of_floors += _value
        return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
print()
print('*************************************************')
print('Конечно же обработку принадлежности к типу слизал')
print('Источник: https://proproprogs.ru/python_oop')
print('*************************************************')