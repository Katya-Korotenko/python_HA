# Одно слово
# Напишите программу, которая обрабатывает список из строк и удаляет все строки,
# содержащие более одного слова, а также преобразует оставшиеся строки к нижнему регистру.
# Данные:
# text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
# Пример вывода:
# Обработанный список: ['hello', 'world', 'simple']


def Aufgabe1():
    text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
    result =[]
    for string in text_list:
        words = string.split()
        if len(words) == 1:
            result.append(string.lower())
    print(result)

#Aufgabe1()



# Обновление цен товаров
# Дан список товаров с ценами. Программа должна применить скидку к каждому товару и
# добавить в список элемент с новой ценой.
# В конце вывести таблицу с новой ценой.
# Данные:
# products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
# Пример вывода:
# Введите скидку (в процентах): 17
# Товар          Старая цена    Новая цена
# Laptop            1200.00$       996.00$
# Mouse                25.00$         20.75$
# Keyboard           75.00$         62.25$
# Monitor            200.00$       166.00$

def Aufgabe2():
    products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
    aktion = float(input('Введите скидку (в процентах):'))
    print("\nТовар   \tСтарая цена\tНовая цена")
    for item in products:
        name = item[0]
        old_price = item[1]
        new_price = old_price * (1 - aktion / 100)
        print(f'{name:<10}{old_price:>10.2f}$ {new_price:>10.2f}$')
Aufgabe2()