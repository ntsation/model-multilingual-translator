import streamlit as st
from transformers import MarianMTModel, MarianTokenizer
import time
import re
import logging  

# Configuração do sistema de logs
logging.basicConfig(
    filename='log.txt',  
    level=logging.INFO,  
    format='%(asctime)s - %(message)s',  
    datefmt='%Y-%m-%d %H:%M:%S'  
)

@st.cache_resource
def load_model(modelo_nome):
    tokenizer = MarianTokenizer.from_pretrained(modelo_nome)
    modelo = MarianMTModel.from_pretrained(modelo_nome)
    return tokenizer, modelo

def sanitize_text(texto):
    texto = re.sub(r"[<>]", "", texto)
    return texto.strip()

def traduzir(texto, modelo_nome):
    tokenizer, modelo = load_model(modelo_nome)
    inputs = tokenizer([texto], return_tensors="pt")
    translated = modelo.generate(**inputs)
    traducao = tokenizer.decode(translated[0], skip_special_tokens=True)
    return traducao

st.title("Tradutor Multilíngue")

idiomas = {
    "Inglês para Espanhol": "Helsinki-NLP/opus-mt-en-es",
    "Espanhol para Inglês": "Helsinki-NLP/opus-mt-es-en",
}
idioma_selecionado = st.selectbox("Selecione o idioma de tradução:", list(idiomas.keys()))


texto_original = st.text_area(
    "Insira o texto para tradução (máximo 500 caracteres):", 
    max_chars=500, 
    height=150
)

if st.button("Traduzir"):
    texto_original = sanitize_text(texto_original)
    if texto_original:
        with st.spinner("Traduzindo..."):
            try:
                modelo_nome = idiomas[idioma_selecionado]
                texto_traduzido = traduzir(texto_original, modelo_nome)

            
                logging.info(f"Texto Original: {texto_original}")
                logging.info(f"Idioma Selecionado: {idioma_selecionado}")
                logging.info(f"Texto Traduzido: {texto_traduzido}")

                st.success("Tradução concluída:")
                st.write(texto_traduzido)

                
                if st.checkbox("A tradução foi útil?"):
                    st.success("Obrigado pelo feedback!")
                else:
                    st.info("Por favor, nos informe como podemos melhorar.")

            except Exception as e:
                st.error(f"Ocorreu um erro durante a tradução: {str(e)}")
                logging.error(f"Erro: {str(e)}")
    else:
        st.warning("Por favor, insira um texto válido para traduzir.")
