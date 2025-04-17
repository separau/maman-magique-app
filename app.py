import streamlit as st
from utils import i18n, letter_generator, image_generator, pdf_exporter, audio_generator

# Language selection
lang = st.sidebar.selectbox("🌐 Language / Langue", ["English", "Français"])
_ = i18n.get_translator(lang)

st.set_page_config(page_title="Maman Magique", layout="centered")

st.title(_("Maman Magique"))

# 1. Lettre personnalisée
st.header(_("💌 Personalized Letter"))
with st.form("letter_form"):
    child_name = st.text_input(_("Your name"))
    mom_name = st.text_input(_("Mom's name"))
    memory = st.text_area(_("A special memory"))
    submitted = st.form_submit_button(_("Generate Letter"))
    if submitted:
        letter = letter_generator.generate_letter(child_name, mom_name, memory, lang)
        st.success(_("Here is your letter:"))
        st.text_area("💖", value=letter, height=300)

# 2. Génération d’image IA
st.header(_("🖼️ AI Image Generator"))
with st.form("image_form"):
    prompt = st.text_input(_("Describe the magical image you want"))
    generate = st.form_submit_button(_("Generate Image"))
    if generate and prompt:
        with st.spinner(_("Generating image...")):
            image_path = image_generator.generate_image(prompt)
            st.image(image_path, caption=_("Generated Image"), use_column_width=True)

# 3. Génération audio
st.header(_("🔊 AI Voice"))
if st.button(_("Generate Audio")):
    if "letter" in locals():
        audio_path = audio_generator.text_to_audio(letter, lang)
        st.audio(audio_path)
    else:
        st.warning(_("Please generate a letter first."))

# 4. Export PDF
st.header(_("📄 Export as PDF"))
if st.button(_("Export Book")):
    if "letter" in locals() and "image_path" in locals():
        pdf_path = pdf_exporter.create_pdf(letter, image_path)
        with open(pdf_path, "rb") as f:
            st.download_button(_("Download PDF"), f, file_name="maman_magique.pdf")
    else:
        st.warning(_("Please generate both a letter and an image."))
