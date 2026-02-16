# Звёздочки вместо чисел
# Напишите программу, которая заменяет все цифры в строке на звёздочки *.
# text = "My number is 123-456-789"
# Пример вывода:
# Строка: My number is 123-456-789
# Результат: My number is ***-***-***


def Aufgabe1():
    text = "My number is 123-456-789 "
    print(f"Строка:{text}")
    for char in text:
        if char.isdigit() :
            text = text.replace(char, '*')
    print(f"Результат:{text}")

# Количество символов
# Напишите программу, которая подсчитывает количество вхождений всех символов в строке.
# Нужно вывести только символы, которые встречаются более 1 раза (игнорируя регистр), с указанием их количества.
# Выводите повторяющиеся символы только один раз.
# text = "Programming in python"
# Пример вывода:
# Строка: Programming in python
# Символ 'p' встречается 2 раз(а)
# Символ 'r' встречается 2 раз(а)
# Символ 'o' встречается 2 раз(а)
# Символ 'g' встречается 2 раз(а)
# Символ 'm' встречается 2 раз(а)
# Символ 'i' встречается 2 раз(а)
# Символ 'n' встречается 3 раз(а)
# Символ ' ' встречается 2 раз(а)
def Aufgabe2():
    text = "Programming in python".lower()
    print(f"Строка: {text}")

    for symbol in set(text):
        count_symbol = text.count(symbol)
        if count_symbol > 1:
            print(f"Символ '{symbol}' встречается {count_symbol} раз(а)")


# Увеличение чисел
# Напишите программу, которая заменяет все числа в строке на их эквивалент, умноженный на 10.
# text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
# Пример вывода:
# I have 50.0 apples and 100.0 oranges, price is 5.0 each. Card number is ....3672.

def Aufgabe3():
    text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
    new_text = []
    for item in text.split():
        if len(item.split('.')) == 2 and item.split('.')[0].isdigit() and item.split('.')[1].isdigit():
            new_text.append(str(float(item)*10))
        elif item.isdigit():
            new_text.append(str(float(item)*10))
        else:
            new_text.append(item)
    print(" ".join(new_text))

Aufgabe1()