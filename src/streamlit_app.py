import streamlit as st

st.set_page_config(page_title="EchoVerse", layout="wide")

st.title("📖 EchoVerse - AI-Powered Audiobook Tool")
st.write("Upload your text, PDF, or DOCX to generate an audiobook with personalized narration.")

uploaded_file = st.file_uploader("Upload a file", type=["txt", "pdf", "docx"])
if uploaded_file:
    st.success(f"Uploaded {uploaded_file.name}")
