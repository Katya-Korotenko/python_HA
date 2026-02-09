
import random
def Aufgabe1():
    num = input('Введите число:')
    sum = 0
    for i in num:
        sum += int(i)
    print(f'Сумма цифр:{sum}')



Aufgabe1()
def Aufgabe2():
    num = input('Введите число:')
    if num == num[::-1]:
        print(f'Число {num} является палиндромом.')
    else:
        print(f'Число {num} не является палиндромом.')

def Aufgabe3():
    print('Угадайте число от 1 до 100. У вас 10 попыток.')
    ran = random.randint(1, 100)
    num = int(input('Ваше предположение:'))
    i = 2

    while i <= 10:
        i += 1
        if num > ran:
            print('Загаданное число меньше вашего')
            num = int(input('Ваше предположение:'))
        elif num < ran:
            print('Загаданное число больше  вашего')
            num = int(input('Ваше предположение:'))
        else:
            print(f'Поздравляем! Вы угадали число: {ran}')
            break
        if i == 10:
            print('Game Over!')

