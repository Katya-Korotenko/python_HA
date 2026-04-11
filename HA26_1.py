import os
import sys

# Список файлов и папок
# Напишите программу, которая принимает путь к директории
# через аргумент командной строки и выводит:
# Отдельно список папок
# Отдельно список файлов
# Пример запуска
# python script.py /home/user/documents
# Пример вывода
# Содержимое директории '/home/user/documents':
# Папки:
# - folder1
# - folder2
# Файлы:
# - file1.txt
# - file2.txt
# - notes.docx

directory = sys.argv[1]
list_files = []
list_directory = []

if len(sys.argv) != 2:
    print("Ошибка: укажите путь к директории.")
    sys.exit()

if not os.path.exists(directory):
    print(f"Ошибка: путь '{directory}' не существует.")
    sys.exit()

if not os.path.isdir(directory):
    print(f"Ошибка: '{directory}' — это не директория.")
    sys.exit()

for item in os.listdir(directory):
    full_path = os.path.join(directory, item)
    if os.path.isfile(full_path):
        list_files.append(item)
    elif os.path.isdir(full_path):
        list_directory.append(item)


print(f"Содержимое директории '{directory}':")

print("Папки:")
for d in list_directory:
    print(f"- {d}")

print("Файлы:")
for f in list_files:
    print(f"- {f}")



