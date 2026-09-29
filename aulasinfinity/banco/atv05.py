import sqlite3
conn = sqlite3.connect(":memory:")
cursos = conn.cursor()

import sqlite3

conexao = sqlite3.connect(":memory:")
cursos = conexao.cursor()

cursos.execute("""
    CREATE TABLE Desempenho (
        curso TEXT,
        aproveitamento INTEGER
    )
""")

dados = [
    ("Python Básico", 90),
    ("SQL Fundamentos", 85),
    ("Python Básico", 70),
    ("SQL Fundamentos", 95)
]

cursos.executemany("""
    INSERT INTO Desempenho (curso, aproveitamento)
    VALUES (?, ?)
""", dados)

conn.commit()
cursos.execute("select aproveitamento from Desempenho")
lista_de_tuplas = cursos.fetchall()
soma = 0
for i in lista_de_tuplas:
    for j in i:
        soma+=j
tamanho = len(lista_de_tuplas)
print(soma/tamanho)
# for i in cursos.fetchall():