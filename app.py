import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers


def GetLLMResponse(input_text,no_words,blog_type):
    llm=CTransformers(model="models\llama-2-7b-chat.ggmlv3.q8_0.bin",
                      model_type='llama',
                      config={'max_new_tokens':200,
                              'temperature':0.01})
    
    template=" wtite a blog for {blog_type} on topic of {input_text} in {no_words} words."
    
    prompt=PromptTemplate(input_variables=['blog_type','input_text','no_words'],template=template)

    response=llm(prompt.format(blog_type=blog_type,input_text=input_text,no_words=no_words))
    return response









st.set_page_config(page_title="Generative AI Blog",
                   layout="centered",
                   initial_sidebar_state='collapsed')
st.header("Blog Generater")

input_text=st.text_input('ENTER THE TOPIC')

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input("ENTER THE NUMBER OF WORDS")

with col2:
    blog_type=st.selectbox("SELECT BLOG FOR",('SCIENTIST','TEACHER','STUDENT'))

submit=st.button("GENERATE")

if submit:
    st.write(GetLLMResponse(input_text,no_words,blog_type))