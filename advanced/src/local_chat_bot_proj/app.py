import os

import streamlit as st
from openai import OpenAI, OpenAIError

MODEL_URL = os.getenv("MODEL_URL", "http://localhost:12434/engines/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "ai/llama3.2")
SYSTEM_PROMPT = "You are a helpful assistant."

client = OpenAI(base_url=MODEL_URL, api_key="not-needed")

st.set_page_config(page_title="Local Chatbot", page_icon="💬")
st.title("💬 Local Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Say something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            stream = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "system", "content": SYSTEM_PROMPT}]
                + st.session_state.messages,
                stream=True,
            )

            def token_generator():
                for chunk in stream:
                    if chunk.choices and chunk.choices[0].delta.content:
                        yield chunk.choices[0].delta.content

            reply = st.write_stream(token_generator())
            st.session_state.messages.append({"role": "assistant", "content": reply})
        except OpenAIError as e:
            st.error(f"Request failed: {e}")