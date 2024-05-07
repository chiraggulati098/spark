import streamlit as st
from txtai.pipeline import Summary

st.set_page_config(layout="wide")

@st.cache_resource
def summary_text(text):
    summary = Summary()
    text = (text)
    return summary(text)

choice = st.sidebar.selectbox("Select your choice", ["Summarize Text","Paraphrase Text","Translate Text"])

# ----- Summarizing -----
if choice == "Summarize Text":
    st.subheader("Summarize Text")
    input_text = st.text_area("Enter your text here")
    if st.button("Summarize Text"):
        col1, col2 = st.columns([1,1])
        with col1:
            st.markdown("**Your Input Text**")
            st.info(input_text)
        with col2:
            st.markdown("**Summarized Text**")
            st.success(summary_text(input_text))

# ----- Paraphrasing -----
elif choice == "Paraphrase Text":
    st.subheader("Paraphrasing Capabilities will be Added in Some Time")

# ----- Translating -----
elif choice == "Translate Text":
    st.subheader("Translate Text")