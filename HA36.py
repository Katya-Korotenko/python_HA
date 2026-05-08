# Класс Person
# Создайте класс Person, представляющий человека.
# Каждый человек должен иметь имя.
# Добавьте метод introduce(), который выводит приветствие с именем.
class Person:
    """
    Личность
    """
    def __init__(self, name: str):
        """
        :param name: имя
        """
        self.name = name


    def introduce(self) -> str:
        """
        Возвращает приветствие с именем.
        :return: строкf с приветствием
        """
        return f"Hallo my name is {self.name}"

# res = Person("Alis")
# print(res.introduce())

# Класс Student
# На основе класса Person создайте класс Student.
# Студент должен иметь имя и номер курса.
# Метод introduce() должен сначала выводить базовое приветствие,
# а затем строку: I'm on course <номер_курса>.


class Student(Person):
    """
    Студент с именем и номером курса
    """

    def __init__(self,name: str, course: int):
        """
        :param name: имя студента
        :param course:  номер курса
        """
        super().__init__(name)
        self.course = course

    def introduce(self) -> str:
        """
        :return: строка с приветствием и номер курса
        """
        intro = super().introduce()
        return f"{intro}\nI'm on course {self.course}"

# res = Student("Alis", 2)
# print(res.introduce())



# Класс Teacher и список людей
# На основе класса Person создайте класс Teacher.
# У преподавателя есть имя и предмет.
# Метод introduce() должен выводить имя и предмет.
# Метод introduce() должен выводить строку: Hello, I am professor <имя>. My subject is <предмет>.
# Создайте список, в котором будут Student и Teacher, и вызовите у всех метод introduce().

class Teacher(Person):
    """
    Преподаватель с  именем и предметом
    """

    def __init__(self, name: str, subject: str):
        """
        :param name: имя преподавателя
        :param subject: название предмета
        """
        super().__init__(name)
        self.subject = subject

    def introduce(self)-> str:
        """
        :return: строка с приветствием, именем преподавателя и его предмет
        """
        return f"Hello, I am professor {self.name}. My subject is {self.subject}."


people = [
    Student("Alice", 2),
    Teacher("Smith", "Math"),
    Student("Ivan", 3),
]

for person in people:
    print(person.introduce())



