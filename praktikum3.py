import math
def Aufgabe1():
    num = float(input('Введите число: '))
    print(f'Округленное вверх: {math.ceil(num)}')
    print(f'Округленное вниз: {math.floor(num)}')


def Aufgabe2():
    num = int(input('Введите число: '))
    i = 0
    list=[]
    while i != num:
        i += 1
        list.append(i)
    print(f'Сумма чисел от 1 до {num}: {sum(list)}')


def Aufgabe3():
    num = int(input("Введите число: "))
    res1 = math.factorial(num)
    print('Факториал числа 5 первым способом:', res1)
    res2 = 1
    while num >= 1:
        res2 *= num
        num -= 1
    print('Факториал числа 5 вторым способом:', res2)
    print('Результаты равны?', res1 == res2)


def Aufgabe4():
    sum = 0
    while True:
        cost = float(input('Введите цену товара: '))
        if cost == 0:
            break
        sum += cost
    print('Сумма покупки:', round(sum))
    a = int(input('Покупатель передал:'))
    print(f'Сдача: {round(a-sum)} евро')


#Учет доходов и расходов
#Напишите программу, которая принимает на вход положительные и отрицательные значения и
#останавливается получив ноль. Программа должна рассчитать сумму доходов (положительные) и расходов
#(отрицательные), а также итоговый баланс.
#Пример вывода:
#Введите доход, расход или '0' для получения итога: 15000
#Введите доход, расход или '0' для получения итога: -5000
#Введите доход, расход или '0' для получения итога: -3000
#Введите доход, расход или '0' для получения итога: 0
#Доходы: 15000
#Расходы: 8000
#Итоговый баланс: 7000

def Aufgabe5():
    sum = 0
    sum_min = 0
    while True:
        cost = int(input('Введите доход, расход или \'0\' для получения итога: '))
        if cost > 0:
            sum = sum + cost
        elif cost < 0:
            sum_min = sum_min - cost
        else:
            print('Доходы: ', sum)
            print('Расходы: ', sum_min)
            break
    print('Итоговый баланс:', sum - sum_min)

def Aufgabe6():
    n = int(input('Введите количество чисел:'))
    a, b = 0, 1
    count = 0

    while count < n:
        print(a, end=' ')
        a, b = b, a + b
        count += 1

def Aufgabe7():
    num = int(input("Введите число: "))
    original = num
    temp = num
    n = 0
    while temp > 0:
        temp //= 10
        n += 1
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        temp //= 10
    if sum == original:
        print("Число", original, "является числом Армстронга.")
    else:
        print("Число", original, "не является числом Армстронга.")

Aufgabe7()
