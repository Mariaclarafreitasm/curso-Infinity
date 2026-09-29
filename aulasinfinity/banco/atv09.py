import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Ativa o uso de chaves estrangeiras no SQLite
cursor.execute("PRAGMA foreign_keys = ON")

# Tabela de cursos
cursor.execute("""
CREATE TABLE cursos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_curso TEXT
)
""")

# Tabela de alunos
cursor.execute("""
CREATE TABLE alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    curso_id INTEGER,
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
)
""")

# Inserindo cursos
cursos = [
    ("Python",),
    ("SQL",),
    ("Java",)
]

cursor.executemany(
    "INSERT INTO cursos (nome_curso) VALUES (?)",
    cursos
)

# Inserindo alunos
alunos = [
    ("Maria", 1),
    ("Luis", 2),
    ("João", 1)
]

cursor.executemany(
    "INSERT INTO alunos (nome, curso_id) VALUES (?, ?)",
    alunos
)

conn.commit()

# INNER JOIN
cursor.execute("""
SELECT alunos.nome, cursos.nome_curso
FROM alunos
INNER JOIN cursos
ON alunos.curso_id = cursos.id
""")

print(cursor.fetchall())

conn.close()