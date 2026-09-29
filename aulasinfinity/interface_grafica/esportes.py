import streamlit as st 

st.title("Escolha seus esportes")
esportes=st.multiselect("Escolha os esportes",['futebol','basquete','volei','natação','tenis'],['futebol','volei'])
