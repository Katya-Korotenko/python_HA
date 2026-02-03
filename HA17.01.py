
def Aufgabe1():
    first = bool(int(input('Enter first value(1-True/0-False): ')))
    second = bool(int(input('Enter second value(1-True/0-False): ')))

    print('value1', 'value2', 'and', 'or', 'not', sep='\t')
    print(first, second, first and second, first or second, not first, sep='\t')

def Aufgabe2():
    licht=bool(int(input('Свет включён?(1-True/0-False): ')))
    window=bool(int(input('Окно открыто?(1-True/0-False): ')))
    print('Свет включён?','Окно открыто?',' Оба условия выполнены?', 'Хотя бы одно условие выполнено?', sep='\t')
    print(licht, window, licht and window, licht or window, sep='\t')


def Aufgabe3():
    Price= 30
    value_mb = float(input('Введите использованные мегабайты:'))
    extra_mb= (value_mb-500)*(value_mb>500)
    result= Price +extra_mb *0.2
    print('Общая стоимость:', result)


