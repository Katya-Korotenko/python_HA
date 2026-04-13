
import logging
logging.basicConfig(
    filename="errors.log",
    encoding="utf-8",
    format="%(asctime)s - %(filename)s - %(levelname)s - %(lineno)d - %(message)s",
    level=logging.ERROR
)

USE_LOGGING = True

# Деление без ошибок
# Напишите функцию, которая выполняет деление двух чисел,
# введенных пользователем, и обрабатывает возможные ошибки.
# Пример вывода:
# Введите делимое: 345
# Введите делитель: 5a
# Ошибка: Введено некорректное число.

def division(number1: str, number2: str) -> float:
    """
    Выполняет деление двух чисел.
    Обрабатывает ошибки ввода и деления на ноль.
    """
    try:
        n1 = float(number1)
        n2 = float(number2)
    except ValueError:
        raise ValueError('Ошибка: Введено некорректное число.')

    if n2 == 0:
        raise ZeroDivisionError('Ошибка: Деление на ноль невозможно.')
    return n1/n2




# Логирование ошибок
# Перенаправьте в предыдущей задаче вывод ошибок в файл errors.log в соответствии с форматом ниже.
# Пример вывода:
# 2025-02-23 22:38:53,686 - ERROR - test.py - 16 - Ошибка: Введено некорректное число.


def division2(number1: str, number2: str) -> float:
    """
    Выполняет деление двух чисел.
    Обрабатывает ошибки ввода и деления на ноль.
    Вывод ошибок перенаправлен в файл errors.log
    """
    try:
        n1 = float(number1)
        n2 = float(number2)
    except ValueError:
        msg = "Ошибка: Введено некорректное число."
        logging.error(msg)
        raise ValueError(msg)

    if n2 == 0:
        msg = "Ошибка: Деление на ноль невозможно."
        logging.error(msg)
        raise ZeroDivisionError(msg)
    return n1/n2


num1 = input("Введите делимое: ")
num2 = input("Введите делитель: ")


try:
    result = division2(num1, num2) if USE_LOGGING else division(num1, num2)
    print(f"Результат: {result}")
except (ValueError, ZeroDivisionError) as e:
    print(e)



