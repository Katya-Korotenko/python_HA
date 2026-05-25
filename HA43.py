# Добавление товаров
# Создайте программу, которая подключается к MongoDB и:
# выбирает базу ich_edit и коллекцию products_<your_group>_<your_full_name>
# очищает коллекцию перед началом
# добавляет 3 товара с полями: name, price, stock
# выводит сообщение о количестве добавленных товаров
# Продолжите предыдущую задачу. Теперь программа должна:
# увеличить цену всех товаров на 20%
# вывести количество обновлённых записей
# затем вывести список всех товаров с новыми ценами
from typing import Any, Mapping

from pymongo import MongoClient
from pymongo.synchronous.cursor import Cursor

products = [
{"name": "Pen", "price": 1.50, "stock": 300},
{"name": "Pencil", "price": 0.99, "stock": 500},
{"name": "Eraser", "price": 0.75, "stock": 200},
]

class ProductDB:
    """
    Класс для работы с коллекцией продуктов в базе данных MongoDB.

    Позволяет:
        - очищать коллекцию,
        - добавлять список продуктов,
        - увеличивать цены на заданный процент,
        - получать все документы из коллекции.
    """

    def __init__(self, connection_string: str, db_name: str, collection_name: str) -> None:
        """
        Инициализирует подключение к MongoDB и выбирает коллекцию.
        :param connection_string: строка подключения к MongoDB.
        :param db_name: имя базы данных.
        :param collection_name: имя коллекции
        """
        self.client = MongoClient(connection_string)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def clear(self) -> None:
        """
        Удаляет все документы из коллекции.
        """
        self.collection.delete_many({})


    def add_products(self, products: list) -> int:
        """
        Добавляет список продуктов в коллекцию.
        :param products: список словарей с данными продуктов.
        :return: количество успешно добавленных документов
        :raise: TypeError если структура продукта некорректна.
        """
        for product in products:
            if not isinstance(product, dict):
                raise TypeError("Product must be a dict")
            elif not isinstance(product.get("name"), str):
                raise TypeError("Field 'name' must be a string")
            elif not isinstance(product.get("price"), (float, int)):
                raise TypeError("Field 'price' must be a float or int")
            elif not isinstance(product.get("stock"), int):
                raise TypeError("Field 'stock' must be a int")

        result = self.collection.insert_many(products)
        return  len(result.inserted_ids)

    def increase_prices(self, percent: float | int ) -> int:
        """
        Увеличивает цену всех продуктов на заданный процент.
        :param percent: процент увеличения
        :return: количество обновлённых документов.
        :return: TypeError если percent не число.
        :return: ValueError если percent <= 0.
        """
        if not isinstance(percent, (int, float)):
            raise TypeError("Percent must be int or float")
        elif percent <= 0 :
            raise ValueError("Percent must be positive")
        formula = 1 + percent / 100
        result = self.collection.update_many({}, {"$mul": {"price": formula}})
        return result.modified_count


    def get_all(self) -> Cursor[Mapping[str, Any]]:
        """
        Возвращает все документы из коллекции.
        :return: Cursor: курсор MongoDB для перебора документов.
        """
        return self.collection.find()



def main():
    """
    Основная функция программы.
    """
    db = ProductDB(
        connection_string = "mongodb://ich_editor:verystrongpassword"
                            "@mongo.itcareerhub.de/?readPreference=primary" 
                            "&ssl=false&authMechanism=DEFAULT&authSource=ich_edit",
        db_name = "ich_edit",
        collection_name = "products_121225ptm_Kateryna"
    )
    db.clear()
    try:
        print(f"{db.add_products(products)} products added.")
        print(f"Price updated for {db.increase_prices(20)} products.")
        print("Updated products:")
        for item in db.get_all():
            print(f"- {item['name']} - ${item['price']:.2f}")
    except (TypeError, ValueError) as e:
        print(e)


if __name__ == "__main__":
    main()