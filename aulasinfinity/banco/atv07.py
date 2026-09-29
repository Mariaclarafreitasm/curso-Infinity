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
    ("Luis","luis@gmail.com")
]

cursos.executemany("insert into alunos (nome,email) values (?,?)",dados)

conn.commit()
cursos.execute("Update alunos set nome = ? ,email = ? where id = ?",("Mariana","mariana@gmail.com",2))
cursos.execute("select * from alunos")
print(cursos.fetchall()) 
