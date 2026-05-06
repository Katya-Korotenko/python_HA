# Класс Rectangle
# Создайте класс Rectangle, который описывает прямоугольник.
# У каждого объекта должны быть два поля: width и height.
# Добавьте метод get_area(), который возвращает площадь прямоугольника.
# Создайте объект прямоугольника с произвольными значениями.
# Выведите его площадь.
# Измените ширину и высоту.
# Выведите новую площадь.

class Rectangle:

    """Класс описывающий прямоугольник с заданной шириной и высотой."""

    def __init__(self ,width: float ,height: float) -> None:
        """
        Прямоугольник

        :param width: ширина прямоугольника
        :param height: высота прямоугольника
        """
        self.width  = width  # поле
        self.height = height

    def get_area(self) -> float:
        """
        Вычисляет площадь прямоугольника

        :return: площадь прямоугольника
        """
        return self.width * self.height


rectangle = Rectangle(10,2)
# print(f"Площадь: {rectangle.get_area()}")
rectangle.height =2
rectangle.width = 15
# print(f"Новая площадь: {rectangle.get_area()}")

# Класс Counter
# Реализуйте класс Counter, который представляет собой простой счётчик.
# Счётчик должен начинаться с нуля.
# Предусмотрите методы для увеличения и уменьшения значения на единицу,
# при этом при каждой операции должно отображаться новое значение счётчика.
# Добавьте метод, возвращающий текущий результат.
# Проверьте работу счётчика, выполнив несколько операций.


class Counter:
    """
    Простой счётчик
    """
    def __init__(self):
        self.count = 0


    def plus(self) -> int:
        """
        Увеличивает счёт
        :return: текущее значение счётчика после увеличения
        """
        self.count += 1
        return self.count

    def minus(self) -> int:
        """
        Уменьшает счёт
        :return: текущее значение счётчика после уменьшения
        """
        self.count -= 1
        return self.count

    def get_count(self) -> int:
        """
        Выводит текущий счёт
        :return: текущее значение счётчика
        """
        return self.count


count = Counter()
print(f"Значение увеличено, текущее:{count.plus()}")
print(f"Значение увеличено, текущее:{count.plus()}")
print(f"Значение увеличено, текущее:{count.plus()}")
print(f"Значение уменьшено, текущее:{count.minus()}")
print(f"Текущее значение:{count.get_count()}")
