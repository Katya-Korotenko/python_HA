# Список всех стран
# Используя базу данных world, выведи названия всех стран из таблицы country.
# Каждое название должно отображаться с новой строки и иметь номер.

# Города выбранной страны
# Добавьте к предыдущей программе возможность выбора страны.
# Пользователь введёт название или номер из выведенного списка.
# Далее выведите все города этой страны и их численность населения, также с нумерацией.

import os

import pymysql
from dotenv import load_dotenv

load_dotenv('.env')

config = {'host': os.getenv('DB_HOST'),
          'user': os.getenv('DB_USER'),
          'password': os.getenv('DB_PASSWORD'),
          'database': os.getenv('DB_NAME'),
          }


class World:
    """
    Класс для работы с базой данных World.
    Атрибуты:
        cur: курсор базы данных, через который выполняются SQL‑запросы.

    Класс предоставляет методы для получения списка стран и городов.
    """

    COUNTRIES_QUERY = """
                      select Name
                      from country; 
                      """

    CITY_QUERY = """
                 select city.Name, city.Population
                 from city
                          JOIN country ON city.CountryCode = country.Code
                 WHERE country.Name = %s
                 ORDER BY city.Population DESC; 
                 """

    def __init__(self, cur) -> None:
        """
        Инициализирует объект World.
        :param cur:Курсор базы данных
        """
        self.cur = cur

    def get_country(self) -> list[str]:
        """
        Получает список всех стран из базы данных.
        :return: Список названий стран.
        """
        self.cur.execute(self.COUNTRIES_QUERY)
        return [row[0] for row in self.cur]

    def get_city(self, country: None | str) -> list[tuple[str, int]]:
        """
        Получает список городов выбранной страны.
        :param country: Название страны.
        :return: Список кортежей (город, население).
        """
        self.cur.execute(self.CITY_QUERY, (country,))
        return [row for row in self.cur]


def print_countries(countries: list[str]) -> None:
    """
    Печатает список стран с нумерацией.
    :param countries: Список стран.
    :return: None:
    """
    for index, country in enumerate(countries, start=1):
        print(f"{index}. {country}")


def print_cities(cities: list[tuple[str, int]]) -> None :
    """
    Печатает список городов с населением.
    :param cities:Список городов и их населения.
    :return: None
    """
    for index, (city, population) in enumerate(cities, start=1):
        print(f"{index}. {city} - {population}")


def prompt_countries(countries: list[str]) -> None | str:
    """
    Запрашивает у пользователя страну или её номер.
    :param countries: Список стран.
    :return: Выбранная страна.
    :raise ValueError: Если введён неверный номер или страна не найдена.
    """
    while True:
        user_input = input('Enter country or country number: ')

        if user_input.isdigit():
            number = int(user_input)
            if 1 <= number <= len(countries):
                return countries[number - 1]
            raise ValueError(f'Country number must be between 1 and {len(countries)}')
        else:
            if user_input in countries:
                return user_input
            raise ValueError('Country not found')


def main() -> None :
    """
    Основная функция программы.

    Подключается к базе данных, выводит список стран,
    запрашивает выбор пользователя и выводит города выбранной страны.
    """
    with pymysql.connect(**config) as conn:
        with conn.cursor() as cur:
            world = World(cur)
            countries = world.get_country()
            print_countries(countries)
            while True:
                try:
                    country = prompt_countries(countries)
                    break
                except ValueError as e:
                    print(e)
            cities = world.get_city(country)
            print_cities(cities)


if __name__ == '__main__':
    main()
