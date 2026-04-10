import logging

# Деление без ошибок
# Напишите функцию, которая выполняет деление двух чисел,
# введенных пользователем, и обрабатывает возможные ошибки.
# Пример вывода:
# Введите делимое: 345
# Введите делитель: 5a
# Ошибка: Введено некорректное число.


def division(num1: float, num2: float) -> float:
    """
        Выполняет деление двух чисел, введённых пользователем.
        Обрабатывает ошибки ввода и деления на ноль.
        """
    try:
        num1 = float(num1)
        num2 = float(num2)
        return num1 / num2
    except ValueError:
        return "Ошибка: Введено некорректное число."
    except ZeroDivisionError:
        return "Ошибка: Деление на ноль невозможно."


num1 = input("Введите делимое: ")
num2 = input("Введите делитель: ")

# print(division(num1, num2))


# Логирование ошибок
# Перенаправьте в предыдущей задаче вывод ошибок в файл errors.log в соответствии с форматом ниже.
# Пример вывода:
# 2025-02-23 22:38:53,686 - ERROR - test.py - 16 - Ошибка: Введено некорректное число.


def division2(num1: float, num2: float) -> float | str:
    """
    Выполняет деление двух чисел, введённых пользователем.
    Обрабатывает ошибки ввода и деления на ноль.
    Вывод ошибок перенаправлен в файл errors.log
    """
    logging.basicConfig(
        filename= "errors.log",
        encoding="utf-8",
        format="%(asctime)s - %(filename)s - %(levelname)s - %(lineno)d - %(message)s ",
        level=logging.ERROR)

    try:
        num1 = float(num1)
        num2 = float(num2)
        return num1 / num2

    except ValueError:
        msg = "Ошибка: Введено некорректное число."
        logging.error(msg)
        return msg
    except ZeroDivisionError:
        msg = "Ошибка: Деление на ноль невозможно."
        logging.error(msg)
        return msg


print(division2(num1, num2))