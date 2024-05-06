import streamlit as st
from transformers import MarianMTModel, MarianTokenizer

modelo_nome = "Helsinki-NLP/opus-mt-en-es"  # Modelo de tradução (Inglês para Espanhol)

tokenizer = MarianTokenizer.from_pretrained(modelo_nome)
modelo = MarianMTModel.from_pretrained(modelo_nome)

def traduzir(texto):
    inputs = tokenizer([texto], return_tensors="pt")
    translated = modelo.generate(**inputs)
    traducao = tokenizer.decode(translated[0], skip_special_tokens=True)
    return traducao

st.title("Tradutor Inglês para Espanhol")

st.write("Insira o texto para traduzir.")

texto_original = st.text_area("Texto para traduzir:")

if st.button("Traduzir"):
    if texto_original.strip():
        texto_traduzido = traduzir(texto_original)
        st.write("Tradução:")
        st.success(texto_traduzido)
    else:
        st.warning("Por favor, insira um texto para traduzir.")
