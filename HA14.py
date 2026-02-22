# Число в конце
# Напишите программу, которая создает новый список.
# В него необходимо добавить только те строки из исходного списка,
# в которых цифры находятся только в конце.
# Данные:
# strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
# Пример вывода:
# Строки с цифрами только в конце: ['apple23', 'grape3']

def Aufgabe1():
    strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
    new_strings = []
    for string in strings:
        head = string.rstrip("1234567890")
        tail = string[len(head):]
        if head.isalpha() and tail:
            new_strings.append(string)
    print(f'Строки с цифрами только в конце:{new_strings}')

#Aufgabe1()
# Удаление кратных
# Напишите программу, которая удаляет из списка все значения,
# кратные числу, которое вводится пользователем.
# Данные:
# numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
# Пример вывода:
# Введите число для удаления кратных ему элементов: 3
# Список без кратных значений: [1, 10, 19, 20]

def Aufgabe2():
    numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
    user_input = int(input("Введите число для удаления кратных ему элементов:"))
    res_numbers = []
    for number in numbers:
        if number % user_input:
            res_numbers.append(number)
    print(res_numbers)

#Aufgabe2()

# Порядок четных
# Напишите программу, которая формирует новый список чисел.
# Добавьте в него все элементы исходного списка, где:
# нечетные числа занимают те же позиции,
# чётные числа отсортированы между собой обратном порядке.
# Данные:
# numbers = [5, 2, 3, 8, 4, 1, 2, 7]
# Пример вывода:
# Список после сортировки: [5, 8, 3, 4, 2, 1, 2, 7]

def Aufgabe3():
    numbers = [5, 2, 3, 8, 4, 1, 2, 7]
    sorted_numbers = sorted([n for n in numbers if n % 2 == 0], reverse=True)
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(sorted_numbers.pop(0))
        else:
            result.append(number)

    print(result)

Aufgabe3()