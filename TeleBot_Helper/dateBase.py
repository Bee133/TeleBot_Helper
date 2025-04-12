import sqlite3

try:
    sqlite_connection = sqlite3.connect('sqlite_python.db',check_same_thread=False)
    sqlite_create_table_query = '''CREATE TABLE sqlitedb_developers (
                                id INTEGER AUTO_INCREMENT PRIMARY KEY,
                                name TEXT,
                                inform TEXT);'''

    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")

    for value in cursor.execute("SELECT * FROM sqlitedb_developers"):
        print(value)


    # cursor.close()
except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
# finally:
#     if (sqlite_connection):
#         sqlite_connection.close()
#         print("Соединение с SQLite закрыто")

    # user_work = input("Название: ")
    # work_inf = input("Описание: ")

    # cursor.execute(f"INSERT INTO sqlitedb_developers (name,inform) VALUES (?,?)",(user_work,work_inf))
    # sqlite_connection.commit()
    # cursor.execute("DELETE FROM sqlitedb_developers WHERE id = 3")
    # sqlite_connection.commit()