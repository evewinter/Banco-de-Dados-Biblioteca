import sqlite3

connection = sqlite3.connect('biblioteca.db')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS Autores;')

cursor.execute('DROP TABLE IF EXISTS Livros;')

cursor.execute('''
    CREATE TABLE Autores (
        autor_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,           
        nacionalidade TEXT
    );
''')

cursor.execute('''
    CREATE TABLE Livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        ano INTEGER,
        autor_id INTEGER,
        FOREIGN KEY (autor_id) REFERENCES Autores(id)
    );
''')

connection.commit()
connection.close()