from langdetect import detect
from deep_translator import GoogleTranslator

# Static dictionaries
translations = {
    "en": {
        "title": "Magical Mom",
        "subtitle": "Your personalized gift for Mother's Day",
        "start_button": "Start creating",
        "upload_photos": "Upload photos",
        "write_letter": "Answer questions to generate the letter",
        "generate_book": "Generate memory book",
        "download_pdf": "Download PDF",
        "listen_audio": "Listen to the message",
    },
    "fr": {
        "title": "Maman Magique",
        "subtitle": "Ton cadeau personnalisé pour la fête des mères",
        "start_button": "Commencer la création",
        "upload_photos": "Importer des photos",
        "write_letter": "Répondre aux questions pour générer la lettre",
        "generate_book": "Générer le livre souvenir",
        "download_pdf": "Télécharger le PDF",
        "listen_audio": "Écouter le message",
    }
}

def translate(key, lang="en"):
    """
    Returns the translated value for a given key and language.
    """
    return translations.get(lang, translations["en"]).get(key, key)

def auto_translate(text, target_lang="en"):
    """
    Translates arbitrary text using Google Translate API (via deep_translator).
    """
    try:
        return GoogleTranslator(source='auto', target=target_lang).translate(text)
    except:
        return text

def get_browser_lang():
    """
    Returns the detected language code from the browser.
    Defaults to 'en' if detection fails.
    """
    try:
        import streamlit.components.v1 as components
        lang = components.html(
            """
            <script>
                const lang = navigator.language || navigator.userLanguage;
                window.parent.postMessage(lang, "*");
            </script>
            """,
            height=0
        )
        return detect(lang)
    except:
        return "en"

def get_translator(lang="en"):
    """
    Returns a _() function to translate keys using selected language.
    """
    def _(key):
        return translate(key, lang)
    return _

