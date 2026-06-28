import streamlit as st
from services.llm import generate_blog

st.set_page_config(
    page_title="Generate Blogs",
    page_icon="🤖"
)

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")

col1, col2 = st.columns(2)

with col1:
    no_words = st.text_input("No of Words")

with col2:
    blog_style = st.selectbox(
        "Writing the blog for",
        ("Researchers", "Data Scientist", "Common People")
    )

if st.button("Generate"):
    if input_text and no_words:
        with st.spinner("Pensando..."):
            st.write_stream(generate_blog(input_text, no_words, blog_style))
    else:
        st.warning("Por favor, rellena todos los campos.")
