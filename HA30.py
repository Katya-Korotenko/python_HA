import json
from datetime import datetime
from typing import Any

# Анализ курсов студентов
# Реализовать программу, которая должна:
# Прочитать файл student_courses.json, содержащий:
# имя,
# дату рождения (birth_date) в формате дд.мм.гггг,
# дату поступления (enrollment_date) в том же формате,
# список курсов.

# Вычислить:
# Общее количество студентов.
# Средний возраст на момент поступления.
# Количество студентов на каждом курсе.
# Сохранить отчёт в JSON-файл student_courses_report.json.


try:
    with open("student_courses.json", "r", encoding="utf-8") as file:
        data = json.load(file)
except FileNotFoundError as e:
    print(e)
    exit()
except json.JSONDecodeError as e:
    print(f"Ошибка чтения JSON: {e}")
    exit()



def report(data: list[dict[str, Any]]) -> dict[str, int |float | dict[str, int ]]:
    """
    Формирует отчёт по студентам и курсам.

    :param data: список, каждый элемент словарь с полями name, birth_date, enrollment_date, courses
    :return: возвращает словарь с тремя ключами
    """


    total_students = len(data)


    total_age = 0
    for student in data:
        enrollment_date = datetime.strptime(student["enrollment_date"], "%d.%m.%Y")
        birth_date = datetime.strptime(student["birth_date"], "%d.%m.%Y")
        age = (enrollment_date - birth_date).days // 365
        total_age += age

    average_age = total_age / total_students


    students_per_course = {}
    for student in data:
        for course in student["courses"]:
            students_per_course[course] = students_per_course.get(course, 0) + 1

    return {
        "total_students": total_students,
        "average_enrollment_age": average_age,
        "students_per_course": dict(sorted(students_per_course.items(), key=lambda x: x[0]))
    }


student_courses_report = report(data)

try:
    with open("student_courses_report.json", "w", encoding="utf-8") as file:
        json.dump(student_courses_report, file, indent=4)
    print("Сохранено в 'student_courses_report.json'.")
except IOError as e:
    print(f"Ошибка при записи файла: {e}")