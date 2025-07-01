import sqlite3

connection = sqlite3.connect('biblioteca.db')
cursor = connection.cursor()

connection.commit()

cursor.execute("SELECT titulo, ano FROM Livros WHERE ano < ?  ORDER BY ano ASC", (1990,))

for Livros in cursor.fetchall():
    print(Livros)

connection.close()