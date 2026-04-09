
from collections import Counter
from collections import defaultdict

# Повторения букв
# Реализуйте функцию, которая принимает текст и возвращает словарь
# с подсчётом количества каждой буквы, игнорируя регистр.
# Данные:


# text = "Programming is fun!"
# Пример вывода:
# {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}


text = "Programming is fun!"

def count_letters(text):
    #вариант без сохранения порядка

    # result = Counter(char for char in text.lower() if char.isalpha())
    # return result

    #второй варинат с сохранением порядка
    counts = Counter(char for char in text.lower() if char.isalpha())

    result = {}
    for char in text.lower():
        if char.isalpha() and char not in result:
            result[char] = counts[char]
    return result



print(count_letters(text))
# Группировка студентов по классам
# Создайте структуру для группировки студентов по классам.
# Добавьте студентов в соответствующие группы.
# Данные:
# students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
# Пример вывода:
# {'class1': ['Alice', 'Charlie'], 'class2': ['Bob'], 'class3': ['Daisy']}


students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]

def clas_students(stedents):

    result = defaultdict(list)
    for class_num, student_name in students:
        result[class_num] = [student_name]

    return dict(result)


print(clas_students(students))
