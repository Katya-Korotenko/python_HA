import re
from typing import Generator

# Извлечение дат
# Реализуйте программу, которая должна:
# Найти в тексте все даты в форматах DD/MM/YYYY, DD-MM-YYYY и DD.MM.YYYY.

text = "The events N 123456 happened on 15/03/2025,01.12.2024  and 09-09-2023. Deadline: 28/02/2022 "

def find_date(text: str) -> Generator[str, None, None]:
    """
    Находит все даты в тексте в форматах DD/MM/YYYY, DD-MM-YYYY, DD.MM.YYYY.

    :param text: текст для поиска дат
    :yield: строка с датой
    """

    dates = re.findall(r"\d{2}[\./-]\d{2}[\./-]\d{4}", text)
    for date in dates:
        yield date

gen = find_date(text)
# for i in gen:
#     print(i)




# Разделение списка тегов
# Реализуйте программу, которая должна:
# Прочитать строку с тегами, введёнными пользователем.
# Разделить её на отдельные теги, независимо от того, чем они были разделены
# (запятые, точки с запятой, слэши или пробелы).
# Удалить лишние пробелы и пустые значения.

tag_input = "python, data-science / machine-learning; AI neural-networks"

def search_tag(text: str) -> list[str]:
    """
    Разделяет строку тегов на отдельные элементы.

    :param text: строка с тегами разделёнными запятыми, точками с запятой, слэшами или пробелами
    :return: список тегов без лишних пробелов и пустых значений
    """

    words = re.split(r"[\s,/;]+", text)
    return words


search = search_tag(tag_input)
print(search)

