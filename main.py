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
        .stTextInput > div > div > input {
            width: 100%;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

st.title("2ndMoon🌙")

inject_custom_css()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages[-10:]:
    if message["role"] == "user":
        st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="response-message">{message["content"]}</div>', unsafe_allow_html=True)

with st.form(key='my_form', clear_on_submit=True):
    question = st.text_input("", placeholder="Ask me anything:", key="question")
    submitted = st.form_submit_button("Send")

    if submitted:
        st.session_state.messages.append({"role": "user", "content": question})
        if question.lower() in knowledge_base:
            response = knowledge_base[question.lower()]
        else:
            try:
                response = model.generate_content(prompt + question).text
            except Exception as e:
                response = f"I'm sorry, I encountered an error while trying to answer that question: {e}"
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()