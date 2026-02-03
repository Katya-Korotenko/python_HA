def Aufgabe1 ():
    x= input('Введите четырехзначное число:')
    sum = 0
    for i in range(len(x)):
        sum += int(x[i])
    print('Сумма цифр числа:', sum )

def Aufgabe2 ():
    a = int(input('Введите первое число:'))
    b = int(input('Введите второе число:'))
    result= a * b
    print(f"Результат:{a * b}-{a}-{b}")
def Aufgabe3 ():
    a = int(input('Введите первое число:'))
    b = int(input('Введите второе число:'))
    temp = a
    while temp >= b:
        temp -= b
    remainder = temp
    print('Остаток от деления:',remainder, 'Целочисленное деление', int(a / b) )

