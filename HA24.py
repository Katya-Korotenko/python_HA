from typing import List, Union

# Сумма цифр числа
# Напишите рекурсивную функцию, которая находит сумму всех цифр числа.
# Пример вывода:
# 24
# Данные:
num = 43197

def sum_num(num: int) -> int:
    """
    Рекурсивно вычисляет сумму всех цифр числа.

    :param num: int Целое число, сумма цифр которого должна быть найдена.
    :return: int Сумма всех цифр числа.
    """

    if num < 10:
        return num
    return num % 10 + sum_num(num // 10)

# print(sum_num(num))

# Сумма вложенных чисел
# Напишите рекурсивную функцию, которая суммирует все числа во вложенных списках.
# Пример вывода:
# 28
# Данные:
nested_numbers = [1, [2, 3], [4, [5, 6]], 7]

def sum_nested_numbers(num: list[Union[int, list]]) -> int:
    """
    Рекурсивно вычисляет сумму всех чисел во вложенных списках.

    :param num:  Список, который может содержать как числа, так и вложенные списки.
    :return: int Сумма всех чисел во всех уровнях вложенности.
    """
    total = 0
    for item in num:
        if isinstance(item, int):
            total += item
        else:
            total += sum_nested_numbers(item)

    return total


#print(sum_nested_numbers(nested_numbers))