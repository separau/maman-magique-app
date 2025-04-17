import streamlit as st
from utils import i18n, letter_generator, image_generator, pdf_exporter, audio_generator

# Set page config
st.set_page_config(
    page_title="Maman Magique",
    page_icon="🌸",
    layout="centered"
)

# Language selector
lang = st.sidebar.selectbox("Language / Langue", ["Français", "English"])
_ = i18n.get_translator(lang)

st.title("🌸 " + _("Maman Magique"))
st.markdown(_("Offrez à votre maman un souvenir magique généré par l'IA !"))

# Step 1: Personalized letter
st.header(_("1. Lettre personnalisée"))
name = st.text_input(_("Votre prénom"))
qualities = st.text_area(_("Décrivez votre maman en quelques mots (qualités, souvenirs, etc.)"))
if st.button(_("Générer la lettre")) and name and qualities:
    letter = letter_generator.generate_letter(name, qualities, lang)
    st.session_state["letter"] = letter
    st.success(_("Lettre générée !"))
    st.text_area(_("Aperçu de la lettre"), letter, height=300)

# Step 2: Album photo
st.header(_("2. Mini-album photo magique"))
uploaded_photos = st.file_uploader(_("Téléversez quelques photos de votre maman"), accept_multiple_files=True, type=["jpg", "jpeg", "png"])
if uploaded_photos:
    styled_images = image_generator.generate_album(uploaded_photos, lang)
    st.session_state["styled_images"] = styled_images
    st.success(_("Photos stylisées prêtes !"))
    for img in styled_images:
        st.image(img, use_column_width=True)

# Step 3: Voix magique (IA)
st.header(_("3. Voix magique"))
if "letter" in st.session_state and st.button(_("Générer la voix de la lettre")):
    audio_path = audio_generator.text_to_audio(st.session_state["letter"], lang)
    st.audio(audio_path)
    st.success(_("Voix générée !"))

# Step 4: Export final
st.header(_("4. Exporter le livre souvenir"))
if st.button(_("Créer le PDF magique")):
    pdf_bytes = pdf_exporter.generate_pdf(
        name=name,
        letter=st.session_state.get("letter", ""),
        images=st.session_state.get("styled_images", []),
        lang=lang
    )
    st.download_button(
        label=_("Télécharger le livre souvenir"),
        data=pdf_bytes,
        file_name="maman_magique.pdf",
        mime="application/pdf"
    )
