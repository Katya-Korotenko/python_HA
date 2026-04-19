# Поиск и удаление дубликатов
# Напишите программу, которая удаляет дублирующиеся строки из файла и сохраняет результат в новый файл.
# Имя нового файла формируется как unique_<original_filename>.
# Если файл не существует, программа должна вывести ошибку.
# Исходный порядок строк должен сохраниться.
# Если в файле нет дубликатов, создаётся точная копия файла.
# Используйте файл movies_to_watch.txt.
# Пример ввода:
# Введите имя файла: movies_to_watch.txt
# Пример вывода:
# Дубликаты удалены. Уникальные строки сохранены в unique_movies_to_watch.txt.



import os

def find_lines(filename: str) -> list[str]:
    """Удаляет дублирующиеся строки из файла."""
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Файл '{filename}' не найден.")

    matches = []
    seen = set()
    with open(filename, mode="r", encoding="utf-8") as file:
        for line in file:
            if line not in seen:
                seen.add(line)
                matches.append(line)

    return matches


filename = input("Введите имя файла для поиска: ")


try:
    matches = find_lines(filename)
    new_filename = f"unique_{filename}"
    with open(new_filename, mode="w", encoding="utf-8") as new_file:
        new_file.writelines(matches)

    print(f"Дубликаты удалены. Уникальные строки сохранены в {new_filename}.")

except FileNotFoundError as e:
    print(e)
except IOError as e:
    print(f"Ошибка при записи файла: {e}")
