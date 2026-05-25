# Создание базы
# Напишите программу, которая:
# создаёт базу данных notes_app_<your_group>_<your_full_name>
# выбирает эту базу через USE notes_app
# выводит сообщение о результате

# Добавление заметок
# Продолжите предыдущую программу:
# создайте таблицу notes с полями: id, title, content
# вставьте одну заметку в таблицу
# выполните commit() после вставки
# выведите все заметки используя DictCursor

import pymysql
from pymysql.cursors import DictCursor

config = {'host': 'ich-edit.edu.itcareerhub.de',
            'user': 'ich1',
            'password': 'ich1_password_ilovedbs',
            'cursorclass': DictCursor
          }



DB_NAME = 'notes_app_121225ptm_Kateryna'
DB_CREATE = f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"
TABLE_CREATE = """CREATE TABLE IF NOT EXISTS notes ( 
                    id INT AUTO_INCREMENT PRIMARY KEY, 
                    title VARCHAR(100), 
                    content VARCHAR(100)
                    )"""

INTO_NOTES = f"""INSERT INTO notes (title, content) VALUES (%s, %s)"""
class Note:
    """
    Класс, представляющий текстовую заметку с идентификатором, заголовком и содержимым
    """
    def __init__(self, id: None, title: str, content: str) -> None:
        """
        Инициализирует объект заметки.
        """
        self.id = id
        self.title = title
        self.content = content

    def __str__(self) -> str:
        """
        Возвращает человекочитаемое строковое представление заметки.
        :return: Краткое описание заметки.
        """
        return f"Note added: {self.title} {self.content}"


def main():
    """
    Основная функция программы.
    """
    with pymysql.connect(**config) as connection:
        with connection.cursor() as cursor:
            cursor.execute(DB_CREATE)
            cursor.execute("SHOW DATABASES")
            databases = [row['Database'] for row in cursor]
            cursor.execute(f"USE {DB_NAME}")
            cursor.execute(TABLE_CREATE)

            if DB_NAME in databases:
                print(f"Database '{DB_NAME}' created or already exists.")

            note = Note(None, "Shopping", "list")
            cursor.execute(INTO_NOTES, (note.title, note.content))
            connection.commit()

            cursor.execute("SELECT * FROM notes")
            notes = [Note(**row) for row in cursor]
            for note in notes:
                print(note)



if __name__ == '__main__':
    main()
