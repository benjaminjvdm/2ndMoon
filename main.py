import streamlit as st
from knowledge_base import knowledge_base
from personality import model, prompt

st.title("2ndMoon: Personalized Q&A")

question = st.text_input("Ask me anything:")

if question:
    st.write(f"You asked: {question}")
    if question.lower() in knowledge_base:
        response = knowledge_base[question.lower()]
    else:
        try:
            response = model.generate_content(prompt + question).text
        except Exception as e:
            response = f"I'm sorry, I encountered an error while trying to answer that question: {e}"
    st.write(f"Response: {response}")