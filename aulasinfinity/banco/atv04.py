import sqlite3
conn = sqlite3.connect(":memory:")
cursos = conn.cursor()

cursos.execute("""
    CREATE TABLE IF NOT EXISTS Pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        regiao TEXT NOT NULL,
        valor REAL NOT NULL
    )
""")

dados = [
    ("Norte", 150.00),
    ("Sul", 200.00),
    ("Norte", 300.00),
    ("Nordeste", 250.00),
    ("Sul", 180.00),
    ("Nordeste", 400.00),
    ("Norte", 120.00),
    ("Sul", 350.00)
]

cursos.executemany("""
    INSERT INTO Pedidos (regiao, valor)
    VALUES (?, ?)
""", dados)

conn.commit()
cursos.execute("select regiao,sum(valor) from Pedidos group by regiao having sum(valor) > 500 ")
for i in cursos.fetchall():
    print(i)