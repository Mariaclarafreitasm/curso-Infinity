import sqlite3
conn = sqlite3.connect(":memory:")
cursos = conn.cursor()

# cursos.execute("""
#     CREATE TABLE IF NOT EXISTS Alunos (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         nome TEXT NOT NULL,
#         nota_final REAL NOT NULL
#     )
# """)
# dados = [
#     ("João", 8.5),
#     ("Maria", 9.0),
#     ("Pedro", 6.5),
#     ("Ana", 7.5),
#     ("Carlos", 5.0)
# ]

# cursos.executemany("""
#     INSERT INTO Alunos (nome, nota_final)
#     VALUES (?, ?)
# """, dados)

# conn.commit()
# cursos.execute("select avg(nota_final),max(nota_final),min(nota_final) from Alunos ")
# for i in cursos.fetchall():
#     print(i)


cursos.execute("""
    CREATE TABLE IF NOT EXISTS Vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vendedor TEXT NOT NULL,
        produto TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        valor REAL NOT NULL
    )
""")

dados = [
    ("João", "Mouse", 2, 80.00),
    ("Maria", "Teclado", 1, 150.00),
    ("João", "Teclado", 2, 150.00),
    ("Pedro", "Mouse", 3, 80.00),
    ("Maria", "Mouse", 2, 80.00),
    ("João", "Monitor", 1, 900.00),
    ("Pedro", "Teclado", 2, 150.00),
    ("Maria", "Monitor", 1, 900.00)
]

cursos.executemany("""
    INSERT INTO Vendas (vendedor, produto, quantidade, valor)
    VALUES (?, ?, ?, ?)
""", dados)

conn.commit()


cursos.execute("select vendedor,sum(valor) from Vendas  group by vendedor having sum(valor) > 400")

for i in cursos.fetchall():
    print(i)