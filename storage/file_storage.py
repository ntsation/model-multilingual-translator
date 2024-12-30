class FileStorage:
    @staticmethod
    def save_translation(original_text, translated_text, language):
        with open("translations.txt", "a") as f:
            f.write(f"Language: {language}\nOriginal Text: {original_text}\nTranslated Text: {translated_text}\n\n")
