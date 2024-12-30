import streamlit as st
from services.translation_service import TranslationService
from services.text_sanitizer import TextSanitizer
from storage.file_storage import FileStorage

def main():
    st.title("Multilingual Translator")

    languages = TranslationService.get_supported_languages()
    selected_language = st.selectbox("Select translation language:", list(languages.keys()))

    original_text = st.text_area("Enter text for translation (max 500 characters):", max_chars=500, height=150)

    if st.button("Translate"):
        sanitized_text = TextSanitizer.sanitize_text(original_text)
        if sanitized_text:
            with st.spinner("Translating..."):
                try:
                    translated_text = TranslationService.translate_text(sanitized_text, selected_language)

                    st.success("Translation completed:")
                    st.write(translated_text)

                    FileStorage.save_translation(sanitized_text, translated_text, selected_language)
                    st.info("The translation was saved successfully.")

                    if st.checkbox("Was the translation helpful?"):
                        st.success("Thank you for your feedback!")
                    else:
                        st.info("Please let us know how we can improve.")

                except Exception as e:
                    st.error(f"An error occurred during translation: {str(e)}")
        else:
            st.warning("Please enter a valid text to translate.")

if __name__ == '__main__':
    main()
