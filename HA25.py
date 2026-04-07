import logging

# Деление без ошибок
# Напишите функцию, которая выполняет деление двух чисел,
# введенных пользователем, и обрабатывает возможные ошибки.
# Пример вывода:
# Введите делимое: 345
# Введите делитель: 5a
# Ошибка: Введено некорректное число.

def division():
    """
    Выполняет деление двух чисел, введённых пользователем.
    Обрабатывает ошибки ввода и деления на ноль.
    """



    try:
        num1 = float(input("Введите делимое:"))
        num2 = float(input("Введите делитель:"))

        result = num1/num2
        print(f"Результат: {result}")

    except ValueError:
        print("Ошибка: Введено некорректное число.")
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль невозможно.")


# division()


# Логирование ошибок
# Перенаправьте в предыдущей задаче вывод ошибок в файл errors.log в соответствии с форматом ниже.
# Пример вывода:
# 2025-02-23 22:38:53,686 - ERROR - test.py - 16 - Ошибка: Введено некорректное число.


def division2():
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
        num1 = float(input("Введите делимое:"))
        num2 = float(input("Введите делитель:"))

        result = num1/num2
        print(f"Результат: {result}")

    except (ValueError, ZeroDivisionError ):

        logging.error(f"Ошибка: Введено некорректное число.")


division2()