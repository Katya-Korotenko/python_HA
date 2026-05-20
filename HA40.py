# Электронное письмо
# Реализуйте класс Email, который представляет электронное письмо. Каждое письмо должно содержать:
# sender — адрес отправителя
# recipient — адрес получателя
# subject — тема письма
# body — текст письма
# date — дата отправки
# Класс должен поддерживать:
# Сравнение писем по дате
# Преобразование письма в строку
# Получение длины текста письма
# Проверку на наличие текста в письме или не состоит ли текст только из пробелов

from datetime import datetime
from functools import total_ordering

@total_ordering
class Email:
    """
    Класс, представляющий электронное письмо.
    Атрибуты:
        sender (str): Адрес отправителя.
        recipient (str): Адрес получателя.
        subject (str): Тема письма.
        body (str): Текст письма.
        date (datetime): Дата и время отправки письма.

    Класс поддерживает сравнение писем по дате отправки,
    а также преобразование в строку, вычисление длины и булеву проверку.
    """

    def __init__(self, sender: str, recipient:str, subject: str, body: str, date: datetime) -> None:
        """
        Инициализирует объект Email.

        :param sender: Отправитель письма.
        :param recipient: Получатель письма.
        :param subject: Тема письма.
        :param body: Текст письма.
        :param date: Дата отправки.
        """
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.date = date

    def __eq__(self, other: object) -> bool:
        """
        Проверяет равенство двух писем по дате отправки.
        :param other: Другой объект для сравнения.
        :return: True, если даты совпадают, иначе False.
        """
        if not isinstance(other, Email):
            return NotImplemented
        return self.date == other.date

    def __lt__(self, other: "Email") -> bool:
        """
        Сравнивает два письма по дате отправки.
        :param other:Другое письмо.
        :return: True, если текущее письмо отправлено раньше.
        """
        return self.date < other.date

    def __str__(self) -> str:
        """
        Возвращает строковое представление письма.
        :return: Форматированная строка с данными письма.
        """
        return f"From: {self.sender}\nTo: {self.recipient}\nSubject: {self.subject}\n- {self.body} -"

    def __len__(self) -> int:
        """
        Возвращает длину текста письма.
        :return:Количество символов в body.
        """
        return len(self.body)

    def __bool__(self) -> bool:
        """
        Определяет, считается ли письмо «непустым»
        :return: True, если тело письма содержит непустой текст.
        """
        return bool(self.body.strip())



# e1 = Email("alice@example.com", "bob@example.com", "Meeting", "Let's meet at 10am", datetime(2024, 6, 10))
# e2 = Email("bob@example.com", "alice@example.com", "Report", "", datetime(2024, 6, 11))
# print(e1)
# print(e1)
# print(e2)
# print("Length:", len(e1))
# print("Has text:", bool(e1))
# print("Is newer:", e2 > e1)



# task2

# Класс для работы с деньгами
# Создайте класс Money, в котором можно:
# складывать и вычитать объекты через операторы + и -
# выводить объект как строку в виде "$<amount>"
# при сложении и вычитании возвращается новый объект
# если вычитание приводит к отрицательному значению — вернуть 0


class Money:
    """
    Класс, представляющий денежную сумму.

    Атрибуты:
        amount (float): Количество денег.

    Класс поддерживает операции сложения и вычитания.
    При вычитании результат не может быть отрицательным — в таком случае возвращается 0.
    """

    def __init__(self, amount: float) -> None:
        """
        Инициализирует объект Money.

        :param amount: Денежная сумма.
        """
        self.amount = amount

    def __add__(self, other: "Money") -> "Money":
        """
        Складывает две денежные суммы.

        :param other: Вторая сумма.
        :return: Новый объект с суммой значений.
        """
        return Money(self.amount + other.amount)

    def __sub__(self, other: "Money") -> "Money":
        """
        Вычитает одну денежную сумму из другой.
        Если результат отрицательный, возвращается Money(0).

        :param other: Сумма, которую нужно вычесть.
        :return: Новый объект с результатом вычитания.
        """
        res = self.amount - other.amount
        if res < 0:
            return Money(0)
        return Money(res)

    def __str__(self) -> str:
        """
        Возвращает строковое представление денежной суммы.

        :return: Строка вида "$<amount>".
        """
        return f"${self.amount}"


money1 = Money(100)
money2 = Money(50)
print(money1 + money2)
print(money1 - money2)
print(money2 - money1)