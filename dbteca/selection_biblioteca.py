import sqlite3

connection = sqlite3.connect('biblioteca.db')
cursor = connection.cursor()

connection.commit()

cursor.execute('SELECT * FROM Autores')
for Autores in cursor.fetchall():
    print(Autores)

connection.close()