import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="FlashApp",
    layout="wide"
)

# Load HTML file
html_file = Path("frontend/index.html")
html_content = html_file.read_text(encoding="utf-8")

st.components.v1.html(
    html_content,
    height=900,
    scrolling=True
)
