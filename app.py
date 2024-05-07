import streamlit as st
from txtai.pipeline import Summary
from deep_translator import GoogleTranslator

language_list = ['chinese (simplified)','french','german','greek','gujarati',
                'hindi','italian','japanese','korean','marathi','portuguese',
                'punjabi','russian','sanskrit','tamil','telugu']

@st.cache_resource
def generate_summary(text):
    summary = Summary()
    return summary((text))

@st.cache_resource
def translate(text,target_lang,input_lang = 'english'):
    return GoogleTranslator(source=input_lang, target=target_lang).translate(text)

# ------------- WEBPAGE DESIGN STARTS HERE -------------

st.set_page_config(layout="wide")

st.title('SPARK - Summarize, Paraphrase, And Rewrite Knowledge')

summarize_tab, paraphrase_tab, translate_tab = st.tabs(["Summarize", "Paraphrase","Translate"])

with summarize_tab:
    st.subheader("Summarize")
    summarize_input = st.text_area('Enter text to Summarize',height=200)
    translate_flag_summarize = st.toggle("Translate the Summary")
    if translate_flag_summarize:
        translate_language_summarize = st.selectbox('Select Language', [x.title() for x in language_list]).lower()
    if st.button('Summarize'):
        col1, col2 = st.columns(2)
        col1.write('Your Input Text')
        col2.write('Generated Summary')
        with col1:
            st.info(summarize_input)
        with col2:
            if translate_flag_summarize:
                st.success(translate(generate_summary(summarize_input),translate_language_summarize))
            else:
                st.success(generate_summary(summarize_input))

with paraphrase_tab:
    pass

with translate_tab:
    st.subheader("Translate")
    tranlate_input = st.text_area('Enter text to Translate',height=200)
    translate_language = st.selectbox('Select Language for Translating', [x.title() for x in language_list]).lower()
    if st.button('Translate'):
        col1, col2 = st.columns(2)
        col1.write('Your Input Text')
        col2.write('Translated Text')
        with col1:
            st.info(tranlate_input)
        with col2:
            st.success(translate(tranlate_input,translate_language))

# st.set_page_config(layout="wide")

# @st.cache_resource
# def summary_text(text):
#     summary = Summary()
#     text = (text)
#     return summary(text)

# choice = st.sidebar.selectbox("Select your choice", ["Summarize Text","Paraphrase Text","Translate Text"])

# # ----- Summarizing -----
# if choice == "Summarize Text":
#     st.subheader("Summarize Text")
#     input_text = st.text_area("Enter your text here")
#     if st.button("Summarize Text"):
#         col1, col2 = st.columns([1,1])
#         with col1:
#             st.markdown("**Your Input Text**")
#             st.info(input_text)
#         with col2:
#             st.markdown("**Summarized Text**")
#             st.success(summary_text(input_text))

# # ----- Paraphrasing -----
# elif choice == "Paraphrase Text":
#     st.subheader("Paraphrasing Capabilities will be Added in Some Time")

# # ----- Translating -----
# elif choice == "Translate Text":
#     st.subheader("Translate Text")