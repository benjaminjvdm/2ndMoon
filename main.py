import streamlit as st
from knowledge_base import knowledge_base
from personality import model, prompt

def inject_custom_css():
    st.markdown(
        """
        <style>
        .user-message {
            background-color: #FFFFFF;
            color: black;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 5px;
            width: fit-content;
            float: right;
            clear: both;
        }
        .response-message {
            background-image: linear-gradient(to right, #4B0082, #800080, #9400D3);
            color: white;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 5px;
            width: fit-content;
            float: left;
            clear: both;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

st.title("2ndMoon: Personalized Q&A")

inject_custom_css()

question = st.text_input("Ask me anything:")

if question:
    st.markdown(f'<div class="user-message">{question}</div>', unsafe_allow_html=True)
    if question.lower() in knowledge_base:
        response = knowledge_base[question.lower()]
    else:
        try:
            response = model.generate_content(prompt + question).text
        except Exception as e:
            response = f"I'm sorry, I encountered an error while trying to answer that question: {e}"
    st.markdown(f'<div class="response-message">{response}</div>', unsafe_allow_html=True)