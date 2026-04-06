# 1. Выбор заказов
# У вас есть список заказов. Каждый заказ содержит название продукта и его цену.
# Напишите функцию, которая:
# Отбирает заказы дороже 500.
# Создаёт список названий отобранных продуктов в алфавитном порядке.
# Возвращает итоговый список названий.
# Пример вывода:
# ['Chair', 'Laptop']
orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}
]

def filter_orders(orders):
    filter = []
    for order in orders:
        if order["price"] > 500:
            filter.append(order["product"])
    return sorted(filter)

# второй вариант
# def filter_orders(orders):
#     return sorted([order["product"] for order in orders if order["price"] > 500])

# print(filter_orders(orders))


# Статистика продаж
# Дан список продаж в виде кортежей (товар, количество, цена).
# Напишите программу, которая:
# Вычисляет общую выручку для каждого товара.
# Возвращает словарь с товарами {товар: выручка}, отсортированный по убыванию выручки.
# Данные:

# Пример вывода:
# {'Chair': 16000, 'Laptop': 6000, 'Monitor': 3000, 'Keyboard': 1500, 'Mouse': 1000}

sales = [

    ("Laptop", 5, 1200),

    ("Mouse", 50, 20),

    ("Keyboard", 30, 50),

    ("Monitor", 10, 300),

    ("Chair", 20, 800)

]

def sales_sum(sales):
    result = {}

    for product, count, price in sales:
        result[product] = count * price

    sorted_revenue = dict(
        sorted(result.items(), key=lambda x: x[1], reverse=True)
    )

    return sorted_revenue




print(sales_sum(sales))



