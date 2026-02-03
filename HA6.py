import math
def Aufgabe1():
    num = float(input('Введите вещественное число: '))
    if num > 0:
        print(f'Округленное значение: {math.ceil(num)}')
    else:
        print(f'Округленное значение: {math.floor(num)}')


def Aufgabe2():
    a = int(input('Введите длину первого катета:'))
    b = int(input('Введите длину второго катета:'))
    result = math.sqrt(a*a + b*b)
    print(result)
    print(f'Длина гипотенузы:{result}')


Aufgabe2()