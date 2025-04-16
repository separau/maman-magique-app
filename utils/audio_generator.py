from gtts import gTTS

def generate_audio(text, voice_type="Adult"):
    tts = gTTS(text=text, lang='en')
    audio_path = "/mnt/data/audio.mp3"
    tts.save(audio_path)
    return audio_path