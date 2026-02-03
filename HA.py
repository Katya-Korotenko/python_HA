
print(1, 2, 3, 4, 5, sep="---")

print("\tПервая строка с табуляцией\nВторая строка на новой строке")

print( 'Это файл "example.txt"')
print( """Это файл "example.txt" """)

first = bool(int(input('first value (1 - True/0 - False)>')))  # '1' -> 1 -> True
second = bool(int(input('second value (1 - True/0 - False)>'))) # '0' -> 0 -> False

print('value 1', 'value 2', 'and', 'or', 'not', sep='\t')
print(first, second, first and second, first or second, not first, sep='\t')


mb = int(input("Введите использованные мегабайты: "))
total = 30 + max(0, mb - 500) * 0.2
print("Общая стоимость:", total)

x= input('Введите четырехзначное число:')
sum = 0
for i in range(len(x)):
    sum += int(x[i])
print('Сумма цифр числа:', sum )

a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
result= a * b
print('Результат:', result,'-',a,'-',b )