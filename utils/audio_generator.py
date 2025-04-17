from gtts import gTTS
import os

def generate_audio(text, lang="en", output_path="output/audio.mp3"):
    """
    Generates an audio file from the given text using gTTS.

    :param text: The text to convert to speech.
    :param lang: Language code ("en" for English, "fr" for French).
    :param output_path: File path to save the audio.
    :return: Path to the generated audio file.
    """
    tts = gTTS(text=text, lang=lang)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    tts.save(output_path)
    return output_path

# Example usage:
# generate_audio("Happy Mother's Day!", lang="en", output_path="output/audio.mp3")

