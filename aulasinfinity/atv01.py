import streamlit as st
import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE nomes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
    )
""")

nomes = [
    "Ana",
    "Carlos",
    "Maria",
    "João",
    "Pedro",
    "Juliana",
    "Lucas",
    "Beatriz",
    "Gabriel",
    "Camila"
]

escolhas = st.selectbox("Escolha um nome", nomes)

if st.button("Atualizar"):
    cursor.execute("""
        INSERT INTO nomes (nome)
        VALUES (?)
    """, (escolhas,))

    conn.commit()

    st.success("Nome adicionado!")