import sqlite3
conn = sqlite3.connect(":memory:")
cursos = conn.cursor()

cursos.execute("""
    CREATE TABLE IF NOT EXISTS estoque (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        preco REAL,
        categoria TEXT
    )
""")

dados = [
    ("Detergente", "Limpeza", 20),
    ("Sabão em pó", "Limpeza", 15),
    ("Desinfetante", "Limpeza", 10),
    ("Água sanitária", "Limpeza", 12),
    ("Esponja", "Limpeza", 30),
    ("Mouse", "Periféricos", 20),
    ("Monitor", "Monitores", 5),
    ("Headset", "Áudio", 15),
    ("Webcam", "Câmeras", 8)
]

cursos.executemany("""
    INSERT INTO Estoque (produto, categoria, quantidade)
    VALUES (?, ?, ?)
""", dados)

conn.commit()

conn.commit()
cursos.execute("select * from estoque order by quantidade DESC ")
for i in cursos.fetchall():
    print(i)