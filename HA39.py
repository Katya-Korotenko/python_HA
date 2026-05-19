# Фигуры и площади
# Создайте абстрактный класс Shape.
# В классе должен быть метод area(), который возвращает площадь фигуры.
# Реализуйте два класса:
# Circle, который принимает радиус.
# Rectangle, который принимает ширину и высоту.
# Проверка размеров фигур
# Доработайте фигуры:
# Добавьте проверку в конструкторы Circle и Rectangle, чтобы значения были положительными.
# Если передано отрицательное или нулевое значение,
# выбрасывайте пользовательское исключение InvalidSizeError.

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    """Абстрактный класс для геометрических фигур."""
    @abstractmethod
    def area(self):
        """Вычисляет площадь фигуры."""
        pass

class Circle(Shape):
    """Класс, представляющий окружность."""

    def __init__(self, radius: float) -> None:
        """
        Создаёт объект окружности.
        :param radius: Радиус окружности (должен быть > 0)
        :raises InvalidSizeError: Если радиус неположительный
        """
        if radius <= 0:
            raise InvalidSizeError ("Радиус должен быть положительным числом")
        self.radius = radius

    def area(self) -> float:
        """
        Вычисляет площадь окружности.
        :return: Площадь круга
        """
        return pi * self.radius ** 2

class Rectangle(Shape):
    """Класс, представляющий прямоугольник."""

    def __init__(self, height: float, width: float) -> None:
        """
        Создаёт объект прямоугольника.

        :param height: Высота прямоугольника (должна быть > 0)
        :param width: Ширина прямоугольника (должна быть > 0)
        :raises InvalidSizeError: Если ширина или высота неположительные
        """
        if height <= 0 or width <= 0:
            raise InvalidSizeError("Ширина и высота должны быть положительными числами")
        self.height: float = height
        self.width: float = width

    def area(self) -> float:
        """
        Вычисляет площадь прямоугольника.
        :return: Площадь (width * height)
        """

        return  self.width * self.height


class InvalidSizeError(Exception):
    """Ошибка, если размер фигуры некорректный."""
    pass



try:
    shapes = [Circle(3), Rectangle(4, 5)]
    for shape in shapes:
        print(f"Area: {shape.area():.2f}")

except InvalidSizeError as e:
    print(e)
