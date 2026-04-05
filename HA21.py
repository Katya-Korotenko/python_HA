# Повторения букв
# Реализуйте функцию, которая принимает текст и возвращает словарь
# с подсчётом количества каждой буквы, игнорируя регистр.
# Данные:


# text = "Programming is fun!"
# Пример вывода:
# {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}


def count_letters():
    text = "Programming is fun!"
    result = {}
    text = text.lower()

    for char in text:
        if char.isalpha():
            if char not in result:
                result[char] = 1
            else:
                result[char] += 1
    return result


# Группировка студентов по классам
# Создайте структуру для группировки студентов по классам.
# Добавьте студентов в соответствующие группы.
# Данные:
# students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
# Пример вывода:
# {'class1': ['Alice', 'Charlie'], 'class2': ['Bob'], 'class3': ['Daisy']}

def clas_students():
    students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
    result = {}
    for class_num, student_name in students:
        if class_num not in result:
            result[class_num] = [student_name]
        else:
            result[class_num].append(student_name)


    return result


print(clas_students())
