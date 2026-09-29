import streamlit as st
import pandas as pd

st.title("Consulta de Funcionários")

dados = {
    "Nome": ["Ana", "Carlos", "Maria", "João", "Pedro", "Julia"],
    "Função": [
        "Desenvolvedor",
        "Designer",
        "Desenvolvedor",
        "Analista",
        "Designer",
        "Desenvolvedor"
    ]
}

df = pd.DataFrame(dados)

st.dataframe(df)

quantidade_funcoes = df["Função"].value_counts()

st.bar_chart(quantidade_funcoes)