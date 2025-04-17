import streamlit as st
from utils.i18n import get_texts
from utils.letter_generator import generate_letter
from utils.image_album import generate_album
from utils.pdf_export import export_pdf
from utils.audio_generator import generate_audio

# Détection de la langue du navigateur
lang = st.query_params.get("lang") or st.session_state.get("lang", "fr")
st.session_state["lang"] = lang
texts = get_texts(lang)

st.set_page_config(page_title=texts["app_title"], layout="centered")

st.title(texts["app_title"])
st.write(texts["app_subtitle"])

menu = st.radio(
    texts["menu_title"],
    [texts["step_letter"], texts["step_photos"], texts["step_result"]],
    key="menu",
)

if menu == texts["step_letter"]:
    with st.form("letter_form"):
        name = st.text_input(texts["form_name"])
        traits = st.text_area(texts["form_traits"])
        memory = st.text_area(texts["form_memory"])
        submit = st.form_submit_button(texts["generate_letter"])
        if submit:
            letter = generate_letter(name, traits, memory, lang)
            st.session_state["letter"] = letter
            st.success(texts["letter_ready"])
            st.text_area(texts["letter_preview"], value=letter, height=300)

elif menu == texts["step_photos"]:
    photos = st.file_uploader(
        texts["upload_photos"],
        accept_multiple_files=True,
        type=["jpg", "jpeg", "png"],
    )
    if photos:
        album = generate_album(photos, lang)
        st.session_state["album"] = album
        st.success(texts["album_ready"])
        for img in album:
            st.image(img, use_column_width=True)

elif menu == texts["step_result"]:
    if "letter" in st.session_state and "album" in st.session_state:
        st.subheader(texts["final_export"])
        if st.button(texts["export_pdf"]):
            pdf_file = export_pdf(st.session_state["letter"], st.session_state["album"], lang)
            st.download_button(texts["download_pdf"], pdf_file, file_name="maman-magique.pdf")

        if st.button(texts["generate_audio"]):
            audio = generate_audio(st.session_state["letter"], lang)
            st.audio(audio, format="audio/mp3")
    else:
        st.warning(texts["need_previous_steps"])
