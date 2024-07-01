import streamlit as st
from transformers import MarianMTModel, MarianTokenizer
import re
import logging

# Configuração do sistema de logs
logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


@st.cache_resource
def load_model(modelo_nome):
    tokenizer = MarianTokenizer.from_pretrained(modelo_nome)
    modelo = MarianMTModel.from_pretrained(modelo_nome)
    return tokenizer, modelo


@st.cache_data
def traduzir_texto(texto, modelo_nome):
    tokenizer, modelo = load_model(modelo_nome)
    inputs = tokenizer([texto], return_tensors="pt")
    translated = modelo.generate(**inputs)
    traducao = tokenizer.decode(translated[0], skip_special_tokens=True)
    return traducao


def sanitize_text(texto):
    # Remove tags HTML e espaços em branco no começo/final
    texto = re.sub(r"[<>]", "", texto).strip()
    return texto


def main():
    st.title("Tradutor Multilíngue")

    idiomas = {
        "Inglês para Espanhol": "Helsinki-NLP/opus-mt-en-es",
        "Espanhol para Inglês": "Helsinki-NLP/opus-mt-es-en",
    }
    idioma_selecionado = st.selectbox(
        "Selecione o idioma de tradução:", list(idiomas.keys()))

    texto_original = st.text_area(
        "Insira o texto para tradução (máximo 500 caracteres):",
        max_chars=500,
        height=150
    )

    if st.button("Traduzir"):
        texto_sanitizado = sanitize_text(texto_original)
        if texto_sanitizado:
            with st.spinner("Traduzindo..."):
                try:
                    modelo_nome = idiomas[idioma_selecionado]
                    texto_traduzido = traduzir_texto(
                        texto_sanitizado, modelo_nome)

                    # Logging
                    logging.info(f"Idioma Selecionado: {idioma_selecionado}")
                    logging.info(f"Texto Original: {texto_sanitizado}")
                    logging.info(f"Texto Traduzido: {texto_traduzido}")

                    # Exibir a tradução
                    st.success("Tradução concluída:")
                    st.write(texto_traduzido)

                    # Feedback
                    if st.checkbox("A tradução foi útil?"):
                        st.success("Obrigado pelo feedback!")
                    else:
                        st.info("Por favor, nos informe como podemos melhorar.")

                except Exception as e:
                    st.error(f"Ocorreu um erro durante a tradução: {str(e)}")
                    logging.error(f"Erro durante a tradução: {str(e)}")
        else:
            st.warning("Por favor, insira um texto válido para traduzir.")


if __name__ == '__main__':
    main()
