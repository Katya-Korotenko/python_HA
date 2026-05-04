import time
from typing import Callable
# Среднее время выполнения
# Создайте декоратор measure_time, который измеряет
# и выводит среднее время выполнения функции за 5 вызовов.
# Функция может быть любой: например, сортировка списка, чтение из файла или расчёты.



def measure_time(func: Callable[[], int]) -> Callable[[], int]:
    """
    Декоратор который измеряет и выводит среднее время выполнения функции за 5 вызовов.
    :param func: функция которую декорируем
    :return: обёрнутая функция которая измеряет среднее время выполнения
    """
    def wrapper() -> int:
        total_time = 0
        for _ in range(5):
            start = time.perf_counter()
            res = func()
            end = time.perf_counter()
            elapsed = end - start
            total_time += elapsed

        average = total_time / 5
        print(f"Среднее время выполнения для 5 вызовов: {average:.6f} сек.")
        return res
    return wrapper

@measure_time
def computer() -> int:
    """
    Считает сумму чисел от 0 до 10 000 000.

    :return: итоговая сумма
    """
    total = 0
    for _ in range(10000000):
        total += 1
    return total


result = computer()
print(f"Результат: {result}")
