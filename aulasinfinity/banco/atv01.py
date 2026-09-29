import sqlite3

conn = sqlite3.connect(":memory:")
cursos = conn.cursor()

cursos.execute("""
    CREATE TABLE IF NOT EXISTS estoque (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL,
        categoria TEXT
    )
""")

cursos.execute("""
    INSERT INTO estoque (produto, quantidade, preco, categoria)
    VALUES (?, ?, ?, ?)
""", ("Teclado", 10, 150.00, "Periféricos"))

dados = [
    ("Mouse", 20, 80.00, "Periféricos"),
    ("Monitor", 5, 900.00, "Monitores"),
    ("Headset", 15, 200.00, "Áudio"),
    ("Webcam", 8, 250.00, "Câmeras")
]

cursos.executemany("""
    INSERT INTO estoque (produto, quantidade, preco, categoria)
    VALUES (?, ?, ?, ?)
""", dados)

conn.commit()

cursos.execute("select * from estoque where produto in ('Monitor')")
for i in cursos.fetchall():
    print(i)
# print(cursos.fetchall())
# Cada tupla dentro de dados representa um produto:

# produto | quantidade | preco | categoria

# O id não precisa ser informado porque ele é AUTOINCREMENT.