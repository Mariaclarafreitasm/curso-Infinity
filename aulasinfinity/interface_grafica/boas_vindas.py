import streamlit as st 
import pandas as pd

dados = {
    "Nome": ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"],
    "Idade": [22, 35, 28, 31, 26],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Salvador"],
    "Profissão": ["Engenheira", "Professor", "Programador", "Médica", "Designer"],
    "Salário": [6500, 4800, 7200, 9800, 5400]
}
df = pd.DataFrame(dados)
st.dataframe(df)
st.title("Seja bem vindo!")
st.header("Sobre este app:")
st.write("Aprendendo sobre streamlit.")
st.divider()
st.header("Interação do usuario")
nome = st.text_input("Qual seu nome:")
if st.button("Cumprimentar"):
    st.success("Ação realizada com sucesso!")
    st.write(f"Ola,{nome}! É um prazer ter voce aqui.")



















# st.markdown("""
#     <style>
#     .stApp{
#     background-color:blue;
#     }
    
#     </style>

# """, unsafe_allow_html=True)
# nome= st.text_input("digite um nome")
# numero= st.number_input("digite um numero")
# data= st.date_input("escolha a data")
# valor= st.slider("escolha a faixa de numero",min_value=0,max_value=100,value=(10,30))
# multi= st.multiselect("escolha as opcoes",["futebol","basquete","tenis"])
# termos= st.checkbox("aceita os termos e condicao")
# if termos:
#     st.success("termos aceito")
# dado = st.radio("escolha oque quer comer",("feijao","lasanha","sushi"))
# with st.sidebar:
#     st.info("info")
#     st.warning("alerta")
#     st.error("erro")

