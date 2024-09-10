import ollama
import streamlit as st

st.title("Ollama Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = ollama.chat(
            model="mistral", messages=st.session_state["messages"],stream=False
            )
        message = response["message"]["content"]
        st.markdown(message)
        st.session_state["messages"].append({"role": "assistant", "content": message})

