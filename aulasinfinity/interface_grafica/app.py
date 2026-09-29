import streamlit as st

st.title("pagina de estudo")
st.write("ola usuario")
if "lista" not in st.session_state:
    st.session_state.lista = []
= st.nometext_input("digite seu nome") 
if st.button("clique"):
    st.success("salvo o nome")
    st.session_state.lista.append(nome)

st.write(st.session_state.lista)