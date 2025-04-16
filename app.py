import streamlit as st
from utils.letter_generator import generate_letter
from utils.image_creator import generate_cover_image
from utils.audio_generator import generate_audio
from utils.pdf_exporter import export_pdf

st.set_page_config(page_title="Maman Magique", layout="centered")

st.title("💖 Maman Magique")
st.write("Create a magical AI-powered gift for your mom.")

name = st.text_input("What’s your mom’s name?")
memory = st.text_area("Share a special memory with your mom")
traits = st.text_area("Describe her in a few words")

uploaded_photos = st.file_uploader("Upload 5-10 photos", type=["jpg", "png"], accept_multiple_files=True)
voice_type = st.selectbox("Choose a voice type", ["Child", "Adult"])

if st.button("Generate Gift"):
    with st.spinner("Creating your magical gift..."):
        letter = generate_letter(name, memory, traits)
        cover = generate_cover_image(name)
        audio = generate_audio(letter, voice_type)
        pdf_path = export_pdf(name, letter, uploaded_photos, cover)
        st.success("Done!")
        st.audio(audio)
        with open(pdf_path, "rb") as f:
            st.download_button("📥 Download the PDF", data=f, file_name="maman_magique_gift.pdf")