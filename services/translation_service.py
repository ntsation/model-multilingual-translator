from transformers import MarianMTModel, MarianTokenizer
from models.translation_model import TranslationModel

class TranslationService:
    @staticmethod
    def get_supported_languages():
        return {
            "English to Spanish": "Helsinki-NLP/opus-mt-en-es",
            "Spanish to English": "Helsinki-NLP/opus-mt-es-en",
            "French to English": "Helsinki-NLP/opus-mt-fr-en",
            "English to French": "Helsinki-NLP/opus-mt-en-fr",
            "German to English": "Helsinki-NLP/opus-mt-de-en",
            "English to German": "Helsinki-NLP/opus-mt-en-de",
        }

    @staticmethod
    def translate_text(text, language):
        model_name = TranslationService.get_supported_languages()[language]
        model = TranslationModel.load_model(model_name)
        inputs = model.tokenizer([text], return_tensors="pt")
        translated = model.model.generate(**inputs)
        return model.tokenizer.decode(translated[0], skip_special_tokens=True)
