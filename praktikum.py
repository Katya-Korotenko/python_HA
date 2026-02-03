
def Aufgabe1():
    name = input('Введите имя:')
    age = input('Введите возраст:')
    color = input('Введите  любимый цвет:')
    print(f'Меня зовут {name}  мне {age} лет, и мой любимый цвет — {color}.')


def Aufgabe2():
    print("Она сказала: \"Привет!\"")
    print('Она сказала: "Привет!"')
    print("""Она сказала: "Привет!\"""")


def Aufgabe3():
    print('Список дел: \n\tУчеба \n\tУборка \n\tСпорт')


def Aufgabe4():
    distans = int(input('Введите расстояние (в км):'))
    speed = int(input('Введите среднюю скорость (в км/ч):'))
    print(f'Время в пути:{distans / speed}')


def Aufgabe41():
    distans = int(input('Введите расстояние (в км):'))
    speed = int(input('Введите среднюю скорость (в км/ч):'))
    time_hours = distans / speed
    hours = int(time_hours)
    minutes = int((time_hours - hours) * 60)
    print(f'Время в пути:{hours} часа и {minutes} минут')


def Aufgabe5():
    total_days = int(input("Введите количество дней до события: "))
    weeks = total_days // 7
    days = total_days % 7
    print(f'До события осталось: {weeks} недель и {days} дня.')


def Aufgabe6():
    distans = int(input('Введите расстояние (в км):'))
    fuel_consumption = int(input('Введите расход бензина на 100 км:'))
    fuel_price = int(input('Введите цену за литр бензина: '))
    total_price = (distans/100)*fuel_price * fuel_consumption
    print(f'Стоимость бензина для поездки:{total_price}')

def Aufgabe7():
    tasks = int(input('Введите количество задач:'))
    time = int(input('Введите среднее время выполнения одной задачи (мин): '))
    total_time = tasks * time
    hours = total_time//60
    minutes = total_time % 60
    print(f'Общее время: {hours} часа и {minutes} минут ')

def Aufgabe8():
    n = input('Введите число: ')
    nn = n+n
    nnn= n+n+n
    result = int(n)+int(nn)+int(nnn)
    print(f'Значение выражения:{result}')

def Aufgabe9():
    n = input('Введите четырёхзначное число: ')
    print(f'Число после изменения:{n[3]}{n[1]}{n[2]}{n[0]}')