import os

# Фильтрация по ключевому слову
# Напишите программу, которая ищет в файле все строки,
# содержащие указанное пользователем слово, и сохраняет их в новый файл.
# Имя нового файла формируется как <keyword>_<original_filename>.
# Если файл не существует, программа должна вывести ошибку.
# Если совпадения не найдены, новый файл не создаётся.
# Используйте файл system_log.txt.
# Пример ввода:
# Введите имя файла для поиска: system_log.txt
# Введите ключевое слово: error
# Пример вывода:
# Строки, содержащие 'error', сохранены в error_system_log.txt.


import os

def find_lines(filename: str, keyword: str) -> list[str]:
    """Возвращает строки файла, содержащие ключевое слово."""
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Файл '{filename}' не найден.")

    matches = []
    with open(filename, mode="r", encoding="utf-8") as file:
        for line in file:
            if keyword.lower() in line.lower():
                matches.append(line)

    return matches


filename = input("Введите имя файла для поиска: ")
keyword = input("Введите ключевое слово: ")

try:
    matches = find_lines(filename, keyword)

    if not matches:
        print("Совпадения не найдены.")
        exit()

    new_filename = f"{keyword}_{filename}"
    with open(new_filename, mode="w", encoding="utf-8") as new_file:
        new_file.writelines(matches)

    print(f"Строки, содержащие '{keyword}', сохранены в {new_filename}.")

except FileNotFoundError as e:
    print(e)
except IOError as e:
    print(f"Ошибка при записи файла: {e}")
