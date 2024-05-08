import streamlit as st
from txtai.pipeline import Summary
from deep_translator import GoogleTranslator
# import torch
# from transformers import PegasusForConditionalGeneration, PegasusTokenizer
# from sentence_splitter import SentenceSplitter, split_text_into_sentences

# model_name = 'tuner007/pegasus_paraphrase'
# torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
# tokenizer = PegasusTokenizer.from_pretrained(model_name)
# model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)
# splitter = SentenceSplitter(language='en')

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

# @st.cache_resource
# def get_response(input_text,num_return_sequences):
#     batch = tokenizer.prepare_seq2seq_batch([input_text],truncation=True,padding='longest',max_length=60, return_tensors="pt").to(torch_device)
#     translated = model.generate(**batch,max_length=60,num_beams=10, num_return_sequences=num_return_sequences, temperature=1.5)
#     tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
#     return tgt_text

# @st.cache_resource
# def paraphrase_text(text):
#     sentence_list = splitter.split(text)
#     paraphrase = []

#     for i in sentence_list:
#         a = get_response(i,1)
#         paraphrase.append(a)

#     paraphrase2 = [' '.join(x) for x in paraphrase]
#     paraphrase3 = [' '.join(x for x in paraphrase2) ]
#     return str(paraphrase3).strip('[]').strip("'")

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

# with paraphrase_tab:
#     st.subheader("Paraphrase")
#     paraphrase_input = st.text_area('Enter text to Paraphrase',height = 200)
#     translate_flag_paraphrase = st.toggle("Translate the Output")
#     if translate_flag_paraphrase:
#         translate_language_paraphrase = st.selectbox('Select Language to Translate', [x.title() for x in language_list]).lower()
#     if st.button('Paraphrase'):
#         col1, col2 = st.columns(2)
#         col1.write('Your Input Text')
#         col2.write('Paraphrased Text')
#         with col1:
#             st.info(paraphrase_input)
#         with col2:
#             if translate_flag_paraphrase:
#                 st.success(translate(paraphrase_text(paraphrase_input),translate_language_paraphrase))
#             else:
#                 st.success(paraphrase_text(paraphrase_input))

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