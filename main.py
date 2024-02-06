import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as gen_ai

#loading enviroment variables
load_dotenv()

#configuring streamlit page
st.set_page_config(
    page_title="Talk with Prabhakar's Gemini-Pro  ",
    page_icon=":brain",
    layout="centered"
)
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

#seing up Google gemini-pro ai model

gen_ai.configure(api_key=GOOGLE_API_KEY)
model=gen_ai.GenerativeModel('gemini-pro')


#Function to translate roles between Gemini-Pro and streamlit terminilogy

def translate_role_for_streamlit(user_role):
    if user_role=="model":
        return "assitant"
    else:
        return user_role

#Intiliaze chat session in Streamlit if nor already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session=model.start_chat(history=[])

#Display the chatbot on webpage
st.title("👻 Prabhakar's gemini Pro -ChatBot")

#Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)


#Input field for user's message
user_prompt=st.chat_input("Ask me....")

if user_prompt:
    # add user message to chat and display it
    st.chat_message("user").markdown(user_prompt)
    gemini_response=st.session_state.chat_session.send_message(user_prompt)

    #Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)
