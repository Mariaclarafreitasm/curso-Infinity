
import sqlite3

conn = sqlite3.connect(":memory:")
cursos = conn.cursor()

cursos.execute("""
    CREATE TABLE Desempenho (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
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
cursos.execute("Update Desempenho set curso = ? ,aproveitamento = ? where id = ?",("python avancado",60,3))
cursos.execute("select * from Desempenho")
print(cursos.fetchall()) 
# lista_de_tuplas = cursos.fetchall()
# soma = 0
# for i in lista_de_tuplas:
#     for j in i:
#         soma+=j
# tamanho = len(lista_de_tuplas)
# print(soma/tamanho)