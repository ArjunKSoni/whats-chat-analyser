import streamlit as st

st.sidebar.title("Whatsapp Chat Analyzer")
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

st.set_page_config(
    title="whatsapp-chat-analyser",
    favicon=": shark:",
)