import re

class TextSanitizer:
    @staticmethod
    def sanitize_text(text):
        return re.sub(r"[<>]", "", text).strip()
