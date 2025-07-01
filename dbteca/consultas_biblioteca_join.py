import sqlite3

connection = sqlite3.connect('biblioteca.db')
cursor = connection.cursor()

print("\n Listar todos os autores com suas nacionalidades: \n")
cursor.execute("SELECT nome, nacionalidade FROM Autores")
for autor in cursor.fetchall():
    print(autor)


# atv 2

print("\n Listar todos os livros mostrando título + nome do autor (com INNER JOIN) \n")
cursor.execute("""
SELECT Livros.titulo, Autores.nome
FROM Livros
INNER JOIN Autores ON Livros.autor_id = Autores.autor_id;
""")
livros_autores = cursor.fetchall()
for livro in livros_autores:
    print(f"Título: {livro[0]}. Autor: {livro[1]}")

# atv 3 

print("\n Listar livros publicados antes de 1950, mostrando título, ano e autor (ORDER BY) ano \n")
cursor.execute("""
SELECT Livros.titulo, Livros.ano, Autores.nome
FROM Livros
INNER JOIN Autores ON Livros.autor_id = Autores.autor_id
WHERE Livros.ano < 1950
ORDER BY Livros.ano ASC;
""")
livros_antigos = cursor.fetchall()
for livro in livros_antigos:
    print(f"{livro[0]}, {livro[1]}, {livro[2]}")

# atv 4 

print("\n Permitir que o usuário informe um título (via input()) e buscar os dados desse livro (título, ano, autor); \n")
titulo_procurado = input("Quer achar o que?: ")

cursor.execute("""
SELECT Livros.titulo, Livros.ano, Autores.nome
FROM Livros
INNER JOIN Autores ON Livros.autor_id = Autores.autor_id
WHERE Livros.titulo = ?;
""", (titulo_procurado,))

resultado = cursor.fetchone()

if resultado:
    print(f"Título: {resultado[0]}. Ano: {resultado[1]}. Autor: {resultado[2]}")
else:
    print("Livro não encontrado.")

# atv 5

print("\n Mostrar quantos livros cada autor tem (agrupado por autor) \n")
cursor.execute("""
SELECT Autores.nome, COUNT(Livros.id) AS total_livros
FROM Autores
LEFT JOIN Livros ON Autores.autor_id = Livros.autor_id
GROUP BY Autores.nome;
""")
qtd_livros_por_autor = cursor.fetchall()
for autor in qtd_livros_por_autor:
    print(f"Autor: {autor[0]}. Total de Livros: {autor[1]}")

connection.close()