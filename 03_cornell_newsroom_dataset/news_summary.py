from summarizer import Summarizer,TransformerSummarizer
import streamlit as st
import numpy as np
import pandas as pd
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_summary(text):
    bert_model = Summarizer()
    summary = ''.join(bert_model(text, min_length = 60))
    return summary


st.title("News Summarization")

st.write('Enter Text')
user_input = st.text_area("Enter text here")
if st.button("Get Summary of text"):
   st.write(get_summary(user_input))

st.write('Enter URL')
url = st.text_input("Enter text here")
if st.button("Get Summary of webpage"):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")
    for script in soup(["script", "style"]):
        script.extract()
    text = soup.get_text()
    st.write(get_summary(text))

docx_file = st.file_uploader("Upload Files", type=['docx', 'txt'])
if st.button("Get Summary of document"):
    raw_text = docx_file.read()
    st.write(get_summary(raw_text))



