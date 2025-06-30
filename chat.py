from llm import get_ai_message
import streamlit as st
from dotenv import load_dotenv

st.set_page_config(page_title="지방세 챗봇",page_icon="🤖")
st.title("🤖 지방세 챗봇")
st.caption("소득세,자동차세,재산세에 관련된 모든것을 답해드립니다!")

load_dotenv()

if 'message_list' not in st.session_state:
    st.session_state.message_list = []

#print(f"before == {st.session_state.message_list}")
for message in st.session_state.message_list:
    with st.chat_message(message["role"]):
        st.write(message["content"])

#def get_ai_message(user_message):
#    return ai_message["result"]

if user_question := st.chat_input(placeholder="지방세에 관련된 궁금한 내용들을 말씀해주세요"):
    with st.chat_message("user"):
        st.write(user_question)
    st.session_state.message_list.append({"role":"user", "content":user_question})

    with st.spinner("답변을 생성하는 중입니다."):
        ai_message = get_ai_message(user_question)
        with st.chat_message("ai"):
            st.write_stream(ai_message)
        st.session_state.message_list.append({"role":"ai", "content":ai_message})
#print(f"after == {st.session_state.message_list}")