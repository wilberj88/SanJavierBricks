import streamlit as st
from streamlit_card import card
from streamlit_extras.grid import grid
from streamlit_extras.colored_header import colored_header
import folium
from streamlit_folium import st_folium
import time
from streamlit_echarts import st_echarts
import pytrends
from pytrends.request import TrendReq
import requests
import random

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="ATENTOS Novus Hotel", page_icon="🧱")
st.title('ATENTOS SanJavierBricks 🧱 Novus Demo')
st.header('🤖🤵🏻Vendedor Virtual🤵🏻‍♂️🤖')
video_file = open('/atento1.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

current_time = time.ctime()
st.write("In real time operation at: ", current_time)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["user"]):
        st.markdown(message["👋Bienvenido a SanJavierBricks, dime cómo sueñas tu proyecto y te ayudaremos a la medida"])
# React to user input
if prompt := st.chat_input("👋Bienvenido a SanJavierBricks, dime cómo sueñas tu proyecto y te ayudaremos a la medida"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        assistant_response = random.choice(
            [
                "Te enviaré a tu correo la propuesta formal para confirmación",
                "Empecemos por lo primero, cómo se llama tu proyecto?",
                "Con gusto lo asesoraremos de la mejor manera desde SanJavierBricks 🧱",
            ]
        )
        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.1)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})


