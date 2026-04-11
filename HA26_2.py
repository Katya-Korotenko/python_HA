import os
import sys

# Поиск и удаление файлов с указанным расширением
# Напишите программу, которая:
# Принимает путь к директории и расширение файлов через аргумент командной строки.
# Рекурсивно ищет файлы с этим расширением во всех вложенных папках.
# Спрашивает у пользователя, хочет ли он удалить найденные файлы.
# Если пользователь подтверждает, удаляет их.
# Пример запуска:
# python script.py /home/user/PycharmProjects/project1 .log
# Пример вывода
# Найдены файлы с расширением '.log':
# - logs/error.log
# - logs/system.log
# - logs/backup/old.log
# - logs/backup/debug.log
# Вы хотите удалить эти файлы? (y/n): y
# Удаление завершено.

def find_files_recursive(directory, extension):
    found = []

    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)

        if os.path.isfile(full_path) and item.endswith(extension):
            found.append(full_path)

        elif os.path.isdir(full_path):
            found.extend(find_files_recursive(full_path, extension))

    return found



if len(sys.argv) != 3:
    print("Использование: python script.py <директория> <расширение>")
    sys.exit()

directory = sys.argv[1]
extension = sys.argv[2]


if not os.path.isdir(directory):
    print("Ошибка: путь не является директорией")
    sys.exit()


files = find_files_recursive(directory, extension)

if not files:
    print("Файлы не найдены")
    sys.exit()

print("Найдены файлы:")
for f in files:
    print(f"- {os.path.basename(f)}")


choice = input("Удалить найденные файлы? (y/n): ").lower()

if choice == "y":
    for f in files:
        os.remove(f)
    print("Файлы удалены")
else:
    print("Удаление отменено")






