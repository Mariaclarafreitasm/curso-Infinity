import sqlite3

conn = sqlite3.connect(":memory:")
cursos = conn.cursor()

cursos.execute("""
    CREATE TABle alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email VARCHAR(45)
    )
""")

dados = [
    ("Maria","maria@gmail.com"),
    ("Mariana","mariana@gmail,com"),
    ("Luis","luis@gmail.com")
]

cursos.executemany("insert into alunos (nome,email) values (?,?)",dados)

conn.commit()
cursos.execute("Delete from alunos where id = 2")

cursos.execute("select * from alunos")
print(cursos.fetchall()) 
