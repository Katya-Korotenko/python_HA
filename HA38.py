#
# Банковский счёт
# Создайте класс BankAccount, описывающий банковский счёт.
# Объект должен хранить имя владельца и текущий баланс.
# Реализуйте методы:
# пополнение счёта
# снятие средств
# отображение баланса
# При попытке снять больше, чем есть на счёте, операция не должна выполняться.
# Продумайте, какие поля и методы следует скрыть от внешнего доступа, а какие оставить открытыми.

# Доработайте класс BankAccount.
# Каждая операция пополнения и снятия должна сохраняться в историю.
# История должна быть доступна через property history только для чтения.
# История представляется в виде списка строк ("Deposit: 150", "Withdraw: 100" и т.д.).


class BankAccount:
    """
    банковский аккаунт с базовыми операциями
    """

    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.__balance = balance
        self.__history = []

    def get_balance(self) -> str:
        """
        Возвращает текущий баланс счёта.
        :return: текущий баланс
        """
        return f"Current balance: {self.__balance}"

    def deposit(self, amount: float) -> str:
        """
        пополнения счета
        :param amount: на какую сумму пополнить
        :return: баланс после пополнения счета
        """
        self.__validate_amount(amount)
        self.__balance += amount
        self.__history.append(f"Deposit: {amount}")
        return self.get_balance()

    def withdraw(self, amount: float) -> str:
        """
        снятие со счета
        :param amount: какую сумму снять со счета
        :return: баланс после снятия счета
        """
        self.__validate_amount(amount)
        if self.__balance >= amount:
            self.__balance -= amount
            self.__history.append(f"Withdraw: {amount}")
            return self.get_balance()
        raise ValueError("Error: Not enough funds.")

    @property
    def history(self) -> str:
        """
        История всех операций только для чтения.
        :return: строка с историей операций
        """
        return f"Operation history:\n\t{"\n\t".join(self.__history)}"

    def __validate_amount(self, amount: float) -> None:
        """
        проверка переменной amount
        :raises ValueError: если сумма отрицательная или равна нулю
        """

        if amount <= 0:
            raise ValueError("Error: Amount must be positive.")



try:
    client1 = BankAccount('Jon', 150)
    print(client1.get_balance())
    print(client1.deposit(50))
    print(client1.withdraw(200))
    print(client1.history)
except ValueError as e:
    print(e)
