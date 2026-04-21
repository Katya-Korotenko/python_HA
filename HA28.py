from typing import Generator
from typing import Iterator
# План по дням недели
# Напишите программу, которая помогает планировать дела.
# Программа должна бесконечно выводить план на следующий день недели,
# пока пользователь нажимает 'Enter'.
# Пример ввода:
# Нажмите 'Enter' для получения плана:
# Monday: Gym, Work, Read book
# Нажмите 'Enter' для получения плана:
# Tuesday: Meeting, Work, Study Python
# Данные:
from itertools import cycle
# Расписание дел на неделю
weekly_schedule = {
    "Monday": ["Gym", "Work", "Read book"],
    "Tuesday": ["Meeting", "Work", "Study Python"],
    "Wednesday": ["Shopping", "Work", "Watch movie"],
    "Thursday": ["Work", "Call parents", "Play guitar"],
    "Friday": ["Work", "Dinner with friends"],
    "Saturday": ["Hiking", "Rest"],
    "Sunday": ["Family time", "Rest"]
}

def weekly_list(weekly_schedule: dict[str,list[str]]) -> None:
    """
    Функция бесконечно выводить план на следующий день недели,
    пока пользователь нажимает 'Enter'.
    :param weekly_schedule: словарь состоящий из строк и списка со строками

    """
    schedule_cycle = cycle(weekly_schedule.items())
    while True:
        user_input = input("Нажмите 'Enter' для получения плана:")
        day, tasks = next(schedule_cycle)
        print(f"{day}: {', '.join(tasks)}")


#weekly_list(weekly_schedule)



# Объединение списков продуктов
# Напишите функцию, которая принимает несколько списков с названиями продуктов и возвращает генератор,
# содержащий все продукты в нижнем регистре.
# Выведите содержимое генератора.
# Данные:
import itertools

fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Tomato", "Cucumber"]
dairy = ["Milk", "Cheese", "Yogurt"]

# первый вариант
# def products_list(*args):
#     return (item.lower() for lst in args for item in lst)
#
# for item in products_list(fruits, vegetables, dairy):
#     print(item)


# второй варинат
def products_list(fruits: list[str],vegetables:list[str],dairy:list[str]) -> Generator[str, None, None]:
    """
    Объединяет списки продуктов и возвращает все элементы в нижнем регистре.
    :param fruits: список фруктов
    :param vegetables: список овощей
    :param dairy: список молочных продуктов
    :return: генератор строк в нижнем регистре
    """
    merged = itertools.chain(fruits,vegetables,dairy)
    return (item.lower() for item in merged)


# for item in products_list(fruits, vegetables, dairy):
#     print(item)


# Комбинации одежды
# Напишите функцию, которая принимает списки типов одежды, цветов и размеров,
# а затем генерирует все возможные комбинации
# в формате "Clothe - Color - Size".
# Данные:

clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]

def combination(clothes:list[str],colors:list[str],sizes:list[str]) -> Iterator[tuple[str, str, str]]:
    """
    Генерирует все возможные комбинации одежды, цвета и размера.

    :param clothes: список типов одежды
    :param colors: список цветов
    :param sizes: список размеров
    :return: итератор кортежей с комбинациями
    """

    pairs = itertools.product(clothes,colors,sizes)
    return pairs

for item in combination(clothes,colors,sizes):
    print("-".join(item))
