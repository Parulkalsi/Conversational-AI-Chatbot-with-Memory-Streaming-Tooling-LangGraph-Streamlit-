import streamlit as st
from langraph_chatbot import chatbot,retreive_all_threads
from langchain_core.messages import HumanMessage,AIMessage,BaseMessage
import uuid


#*******************************************Utility functions ********************************************

def generate_thread_id():
    thread_id =str(uuid.uuid4())
    return thread_id

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    st.session_state['chat_threads'] = retreive_all_threads()
    st.session_state['message_history'] = []

def load_coversations(thread_id):
    return chatbot.get_state(config = {'configurable': {'thread_id': thread_id}}).values['messages']


#*******************************************Session setup ********************************************
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if "thread_id" not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if "chat_threads" not in st.session_state:
    st.session_state['chat_threads'] = retreive_all_threads()



#********************************************Side Bar UI **********************************************

st.sidebar.title("Chatbot")

if st.sidebar.button("New Chat"):
    reset_chat()

st.sidebar.header("My conversation")

for thread_id in st.session_state['chat_threads'][::-1]:
    if st.sidebar.button(thread_id):
        st.session_state['thread_id'] = thread_id
        messages = load_coversations(thread_id)

        temp_messages = []

        for msg in messages:
            if isinstance(msg,HumanMessage):
                role = "user"
            else:
                role = "assistant"
            temp_messages.append({"role": role, "content": msg.content})

        st.session_state['message_history'] = temp_messages

threads = retreive_all_threads()




#*******************************************Main UI **************************************************

CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])


user_message = st.chat_input("Type your message here...")
if user_message:
    st.session_state['message_history'].append({"role":"user","content":user_message})
    with st.chat_message("user"):
        st.text(user_message)
    
    
    with st.chat_message("assistant"):
      def ai_only_stream():
        for message_chunk, metadata in chatbot.stream ({'messages':[HumanMessage(content=user_message)]},config = CONFIG,stream_mode = 'messages'):
            if isinstance(message_chunk,AIMessage):
                yield message_chunk.content

    ai_message = st.write_stream(ai_only_stream())

st.session_state['message_history'].append({"role":"assistant","content": ai_message})

