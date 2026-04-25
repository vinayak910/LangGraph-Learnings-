import streamlit as st 
from streamlit_backend import chatbot
from langchain_core.messages import HumanMessage

CONFIG = {'configurable':{'thread_id': 'thread-1'}}

user_input = st.chat_input("Type here")

if user_input: 

    st.session_state['message_history'].append({'role':'user' , 'content':user_input})

    with st.chat_message('user'):
        st.text(user_input)

    response = chatbot.invoke({'messages':[HumanMessage(content = user_input)]}, config= CONFIG)

    ai_message = response['messages'][-1]

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})
    with st.chat_message('assistant'):
        st.text(ai_message)