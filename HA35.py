# Счётчик экземпляров
# Создайте класс User, представляющий пользователя.
# При создании должны указываться логин (username) и пароль (password).
# У класса должно быть поле total_users, хранящее общее количество созданных пользователей.
# При каждом создании нового объекта User, счётчик должен увеличиваться.
# Добавьте метод get_total(), возвращающий количество пользователей.
# Проверьте, что счётчик работает.

class User:
    """
    Пользователь с полями имя и пароль

    """

    total_users = 0
    def __init__(self, username: str, password: int):
        """
        :param username: имя пользователя
        :param password: пароль пользователя
        """
        self.username = username
        self.password = password
        User.total_users += 1

    @classmethod
    def get_total(cls) -> int:
        """
        Возвращает общее количество созданных пользователей.
        :return: количество пользователей
        """
        return cls.total_users


# user = User("Katy", 12345)
# user2 = User("Ivan", 12345)
#
# print(f"Kоличество пользователей:{user.get_total()} ")
# print(user.__dict__)


# Проверка данных пользователя
# Доработайте класс User.
# Добавьте валидации полей при создании.
# Имя должно быть непустой строкой.
# Пароль должен быть строкой длиной не менее 5 символов.
# Если данные некорректны — выбрасывайте ValueError.
# Добавьте строковое представление объекта.
# Проверьте работу класса с разными значениями.



class User2:
    """
    Пользователь с полями имя и пароль

    """

    total_users = 0
    def __init__(self, username: str, password: str):
        """
        :param username: имя пользователя
        :param password: пароль не менее 5 символов
        :raises ValueError: если имя пустое или пароль короче 5 символов
        """

        if not username.strip():
            raise ValueError("Имя не может быть пустым")

        if len(password) < 5:
            raise ValueError(f"Недопустимый пaроль: {password}")

        self.username = username
        self.password = password
        User2.total_users += 1

    @classmethod
    def get_total(cls) -> int:
        """
        :return: количество пользователей
        """
        return cls.total_users

    def __str__(self) -> str:
        """
        Строковое представление пользователя.
        :return: строка с именем пользователя
        """

        return f"User: {self.username}"


try:
    user = User2("Katy", "fg")
    print(user)
except ValueError as e:
    print(e)

try:
    user2 = User2("Ivan", "12345")
    print(user2)
    print(f"Количество пользователей: {User2.get_total()}")
except ValueError as e:
    print(e)

