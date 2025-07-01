import sqlite3

connection = sqlite3.connect('biblioteca.db')
cursor = connection.cursor()

buscar = 'Penelpe Douglas'

cursor.execute('SELECT * FROM Autores WHERE nome = ?', (buscar,))

Autores = cursor.fetchone()

if Autores:
    print('Nome encontrado:', Autores)
else:
    print('Nome não encontrado.')

connection.close()