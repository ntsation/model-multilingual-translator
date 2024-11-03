import streamlit as st
from transformers import MarianMTModel, MarianTokenizer
import re
import logging
import os

logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

@st.cache_resource
def load_model(model_name):
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model

@st.cache_data
def translate_text(text, model_name):
    tokenizer, model = load_model(model_name)
    inputs = tokenizer([text], return_tensors="pt")
    translated = model.generate(**inputs)
    translation = tokenizer.decode(translated[0], skip_special_tokens=True)
    return translation

def sanitize_text(text):
    text = re.sub(r"[<>]", "", text).strip()
    return text

def save_translation(original_text, translated_text, language):
    with open("translations.txt", "a") as f:
        f.write(f"Language: {language}\nOriginal Text: {original_text}\nTranslated Text: {translated_text}\n\n")

def main():
    st.title("Multilingual Translator")

    languages = {
        "English to Spanish": "Helsinki-NLP/opus-mt-en-es",
        "Spanish to English": "Helsinki-NLP/opus-mt-es-en",
        "French to English": "Helsinki-NLP/opus-mt-fr-en",
        "English to French": "Helsinki-NLP/opus-mt-en-fr",
        "German to English": "Helsinki-NLP/opus-mt-de-en",
        "English to German": "Helsinki-NLP/opus-mt-en-de",
    }
    selected_language = st.selectbox("Select translation language:", list(languages.keys()))

    original_text = st.text_area("Enter text for translation (max 500 characters):", max_chars=500, height=150)

    if st.button("Translate"):
        sanitized_text = sanitize_text(original_text)
        if sanitized_text:
            with st.spinner("Translating..."):
                try:
                    model_name = languages[selected_language]
                    translated_text = translate_text(sanitized_text, model_name)

                    logging.info(f"Selected Language: {selected_language}")
                    logging.info(f"Original Text: {sanitized_text}")
                    logging.info(f"Translated Text: {translated_text}")

                    st.success("Translation completed:")
                    st.write(translated_text)

                    save_translation(sanitized_text, translated_text, selected_language)
                    st.info("The translation was saved successfully.")

                    if st.checkbox("Was the translation helpful?"):
                        st.success("Thank you for your feedback!")
                    else:
                        st.info("Please let us know how we can improve.")

                except Exception as e:
                    st.error(f"An error occurred during translation: {str(e)}")
                    logging.error(f"Error during translation: {str(e)}")
        else:
            st.warning("Please enter a valid text to translate.")

if __name__ == '__main__':
    main()
