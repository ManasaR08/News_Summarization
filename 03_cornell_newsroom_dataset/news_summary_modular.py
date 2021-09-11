from summarizer import Summarizer,TransformerSummarizer
import streamlit as st
import numpy as np
import pandas as pd
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup

# """
# This is a model for generating Abstractive summary on a topic you can upload a file or paste alink or paste a text to generate summary. We have used BERT model to generate the summary. BERT, which stands for Bidirectional Encoder Representations from Transformers, is based on Transformers, a deep learning model in which every output element is connected to every input element, and the weightings between them are dynamically calculated based upon their connection. (In NLP, this process is called attention.)

# Historically, language models could only read text input sequentially -- either left-to-right or right-to-left -- but couldn't do both at the same time. BERT is different because it is designed to read in both directions at once. This capability, enabled by the introduction of Transformers, is known as bidirectionality. 

# Using this bidirectional capability, BERT is pre-trained on two different, but related, NLP tasks: Masked Language Modeling and Next Sentence Prediction.

# The objective of Masked Language Model (MLM) training is to hide a word in a sentence and then have the program predict what word has been hidden (masked) based on the hidden word's context. The objective of Next Sentence Prediction training is to have the program predict whether two given sentences have a logical, sequential connection or whether their relationship is simply random.
# """

class main_obj(object):

    def __init__(self):
        st.title("News Summarization")

    def get_summary(self, text):
        self.text = text
        bert_model = Summarizer()
        summary = ''.join(bert_model(self.text, min_length = 60))
        return summary


class stramlit_obj(main_obj):

    def __init__(self):
        st.title("News Summarization")
        st.write('Enter Text')
        self.text = st.text_area("Enter text here")
        if st.button("Get Summary of text"):
           st.write(main_obj.get_summary(self, self.text))

        st.write('Enter URL')
        url = st.text_input("Enter text here")
        if st.button("Get Summary of webpage"):
            html = urlopen(url).read()
            soup = BeautifulSoup(html, features="html.parser")
            for script in soup(["script", "style"]):
                script.extract()
            self.text = soup.get_text()
            st.write(main_obj.get_summary(self, self.text))

        docx_file = st.file_uploader("Upload Files", type=['docx', 'txt'])
        if st.button("Get Summary of document"):
            self.raw_text = docx_file.read()
            st.write(main_obj.get_summary(self, self.raw_text))


#run_obj1 = main_obj()
run_obj = stramlit_obj()


    






   











