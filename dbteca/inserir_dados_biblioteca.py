import sqlite3

connection = sqlite3.connect('biblioteca.db')
cursor = connection.cursor()

Autores = [
    ("R.F. Kuang", "China"),
    ("Mona Awad", "USA"),
    ("Penelpe Douglas", "USA"),
    ("Machado de Assis", "Brasileiro"), 
    ("Rachel de Queiroz", "Brasileira"), 
    ("George Orwell", "Britânico"), 
    ('Clarice Lispector', 'Ucraniana'), 
    ('Gabriel García Márquez', 'Colombiano'), 
    ('José Saramago', 'Português'),
    ('Stephen King', 'Americano'), 
    ('Chimamanda Ngozi Adichie', 'Nigeriana'), 
    ('Agatha Christie', 'Britânica'), 
    ('Jorge Amado', 'Brasileiro'), 
    ('Isabel Allende', 'Chilena'), 
    ('Haruki Murakami', 'Japonês'), 
    ('Dan Brown', 'Americano'), 
    ('Neil Gaiman', 'Britânico') 
]

cursor.executemany("INSERT INTO Autores (nome, nacionalidade) VALUES (?, ?)", Autores)

connection.commit()

Livros = [
    ("Babel", "2024", "001"),
    ("Corrupt", "2022", "002"),
    ("Hideway", "2023", "003"),
    ("Kill Switch", "2024", "004"),
    ("Nightfall", "2024", "005"),
    ("Dom Casmurro", "1899", "006"), 
    ("Dom Casmurro", "1899", "007"),  
    ('Memórias Póstumas de Brás Cubas', '1881', '008'),  
    ('O Quinze', '1930', '009'),  
    ('1984', '1949', '010'),  
    ('A Revolução dos Bichos', '1945', '011'),  
    ('A Hora da Estrela', '1977', '012'),  
    ('Cem Anos de Solidão', '1967', '013'),  
    ('O Amor nos Tempos do Cólera', '1985', '014'),  
    ('Ensaio sobre a Cegueira', '1995', '015'),  
    ('Harry Potter e a Pedra Filosofal', '1997', '016'),  
    ('Harry Potter e a Câmara Secreta', '1998', '017'),  
    ('It - A Coisa', '1986', '018'),  
    ('Carrie', '1974', '019'),  
    ('Americanah', '2013', '020'),  
    ('O Assassinato de Roger Ackroyd', '1926', '021'),  
    ('Assassinato no Expresso do Oriente', '1934', '022'),  
    ('Gabriela, Cravo e Canela', '1958', '023'),  
    ('Capitães da Areia', '1937', '024'),  
    ('A Casa dos Espíritos', '1982', '025'),  
    ('Kafka à Beira-Mar', '2002', '026'),  
    ('1Q84', '2009', '027'),  
    ('O Código Da Vinci', '2003', '028'),  
    ('Anjos e Demônios', '2000', '029'),  
    ('Deuses Americanos', '2001', '030')
]

cursor.executemany("INSERT INTO Livros (titulo, ano, autor_id) VALUES (?, ?, ?)", Livros)

connection.commit()

connection.close()