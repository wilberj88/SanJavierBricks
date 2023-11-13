import streamlit as st
from streamlit_extras.let_it_rain import rain 
from streamlit_echarts import st_echarts
import plotly.graph_objects as go
import folium
import time
import datetime
import pandas as pd
import numpy as np
from PIL import Image
from streamlit_extras.colored_header import colored_header
from streamlit_extras.grid import grid


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="SanJavierBricks demo Novus", page_icon="🧱")

with st.sidebar:
    image = Image.open('SanJavierBricks.jpeg')
    st.image(image, caption='Demo Novus Mando: Monitor en Tiempo Real de Productividad Actual Vs Histórica. Alarmas y Recomendaciones para Planta Zamora 🏭')

st.title('Estrategia de Datos e Inteligencia Artificial - Planta Zamora 🧱')

st.markdown(
  """
  - 🗣️ _    Titularidad
  - ♻️ _    Ciclo de Vida
  - 🏗️ _     Arquitectura
  - 🧮 _     Modelación
  - ⏲️ _     Operación
  - 🛂 _     Seguridad
  - 🚫 _     Privacidad
  - 🤝 _     Conciliación
  - 💡 _     Referentes
  - 🌊 _     Lago
  - ⚠️ _     Elementos Críticos
  - ℹ️ _     Metadata
  - ✅ _     Calidad
  - 🔄 _     Integración
  - ✝️ _     Políticas
  - ▶️ _     Estándares
  - 🔁 _     Procesos
  
  DISFRUTA TU ECOSISTEMA INTEROPERABLE AHORA 🕰
  """
)
