def Aufgabe():
    first = int(input('Введите первое число: '))
    second = int(input('Введите второе число: '))
    third = int(input('Введите третье число: '))
    numbers = [first, second, third]

    if numbers == sorted(numbers):
        print('Числа отсортированы по порядку')
    else:
        print('Числа не по порядку')

def Aufgabe1():
    num1=int(input('Введите первое число:'))
    num2 = int(input('Введите второе число:'))
    num3 = int(input('Введите третье число:'))
    if num1<num2<num3:
        print('Числа упорядочены по возрастанию.')
    else:
        print('Числа не упорядочены по возрастанию')

def Aufgabe2():
    num1 = int(input('Введите первое число:'))
    num2 = int(input('Введите второе число:'))
    if num1>num2:
        print(f'Большее число:{num1}')
    elif num1<num2:
        print(f'Большее число:{num2}')
    else:
        print('Числа равны ')

def Aufgabe3():
    num = int(input('Введите число:'))
    if num % 2:
        print('Нечетное')
    else:
        print('Четное')

def Aufgabe31():
    num = int(input('Введите число:'))
    print( 'Нечетное' if num%2 else 'Четное' )



def Aufgabe4():
    age = int(input('Введите возраст:'))
    if age <= 12:
        print('Вы ребенок')
    elif age <= 18:
        print('Вы подросток')
    elif age <= 60:
        print('Вы взрослый')
    else:
        print('Вы пожилой')

def Aufgabe5():
    num1 = int(input('Введите первое число:'))
    num2 = int(input('Введите второе число:'))
    num3 = int(input('Введите третье число:'))
    if num1+num2 > num3 or num2+num3 > num1 or num1+num3 > num2:
        print('Такой треугольник может существовать.')
    else:
        print('Такой треугольник не может существовать.')




def Aufgabe6():
    string = input('Введите строку')
    print( 'Строка пуста' if string == "" else "Строка заполнена")


def Aufgabe7():
    num1 = int(input('Введите координату x:'))
    num2 = int(input('Введите координату y:'))
    if num1 > 0 and num2 > 0:
        print('B 1 квадранте')
    elif num1 < 0 and num2 > 0:
        print('B 2 квадранте')
    elif num1 < 0 and num2 < 0:
        print('B 3 квадранте')
    elif num1 > 0 and num2 < 0:
        print('B 4 квадранте')

    else:
        print('На оси')

def Aufgabe8():
    num1 = int(input('Введите часы:'))
    num2 = int(input('Введите минуты:'))
    if num1< 24 and num2 < 60:
        print('корректное время')
    else:
        print('Некорректное время.')








