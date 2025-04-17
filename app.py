import streamlit as st
from utils import i18n, letter_generator, image_album, pdf_export, audio_generator

# Détecte la langue automatiquement
lang = i18n.detect_language()
_ = i18n.get_translator(lang)

st.set_page_config(page_title=_("Maman Magique"), layout="centered")

st.image("assets/logo.png", width=200)

st.title(_("Maman Magique"))
st.write(_("Créez un souvenir magique pour votre maman."))

with st.form("memory_form"):
    name = st.text_input(_("Prénom de la maman"))
    sender = st.text_input(_("Votre prénom"))
    memories = st.text_area(_("Décrivez quelques souvenirs ou moments marquants"))
    photos = st.file_uploader(_("Ajoutez 5 à 10 photos"), accept_multiple_files=True, type=["jpg", "jpeg", "png"])
    voice = st.selectbox(_("Choisissez la voix pour l’audio"), ["Enfant", "Adulte"])
    submitted = st.form_submit_button(_("Générer"))

if submitted:
    with st.spinner(_("Génération du livre souvenir...")):
        letter = letter_generator.generate_letter(name, sender, memories, lang)
        album = image_album.generate_album(photos, lang)
        cover = image_album.generate_cover(name, lang)
        pdf_path = pdf_export.create_pdf(name, letter, album, cover, lang)
        audio_path = audio_generator.create_audio(letter, voice, lang)

    st.success(_("Livre généré avec succès !"))
    st.download_button(_("Télécharger le livre (PDF)"), data=open(pdf_path, "rb"), file_name="Maman_Magique.pdf")
    st.audio(audio_path)
