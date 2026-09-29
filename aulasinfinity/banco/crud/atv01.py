import streamlit as st

st.title("App")

nome = st.text_input("digite seu nome")
funcao = st.text_input("digite sua função") 

if st.button("clique"):
    st.success("salvo")

