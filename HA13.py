# Прогрессия увеличения
# Напишите программу, которая создаёт новый кортеж, состоящий из элементов изначального в том же порядке.
# Добавить в него только элементы, которые больше всех предыдущих значений в исходном кортеже.
# Данные:
# numbers = (3, 7, 2, 8, 5, 10, 1)
# Пример вывода:
# Кортеж по возрастанию: (3, 7, 8, 10)
from operator import index
from os.path import sep
from traceback import print_exc


def Aufgabe1():
    numbers = (3, 7, 2, 8, 5, 10, 1)
    res = ()
    max_value = numbers[0]
    res += (max_value,)
    for index, value in enumerate(numbers[1:]):
        if value > max_value:
            res += (value,)
            max_value = value
    print(res)
#Aufgabe1()

# Повторяющиеся элементы
# Напишите программу, которая находит индексы элементов кортежа, встречающихся более одного раза.
# Вывести сами элементы и их индексы.
# Данные:
# numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
# Пример вывода:
# Индексы элемента 2: 1 4 9
# Индексы элемента 3: 2 6
# Индексы элемента 4: 3 8

def Aufgabe2():
    numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
    printed = ()
    for index, value in enumerate(numbers):
        if numbers.count(value) > 1 and value not in printed:
            tuple_index = ()
            for i, v in enumerate(numbers):
                if v == value:
                    tuple_index += (i,)
            print(f"Индексы элемента {value}:", *tuple_index )
            printed += (value,)


Aufgabe2()