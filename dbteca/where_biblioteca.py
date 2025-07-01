import sqlite3

connection = sqlite3.connect('biblioteca.db')
cursor = connection.cursor()

buscar = 'Hideway'

cursor.execute('SELECT * FROM Livros WHERE titulo = ?', (buscar,))

livro = cursor.fetchone()

if livro:
    print('Livro encontrado:', livro)
else:
    print('Livro não encontrado.')

connection.close()