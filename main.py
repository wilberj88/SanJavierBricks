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

st.title('Piloto de Monitoreo y Optimización en Tiempo Real - Planta Zamora 🧱')

st.write('---')
st.write("""
**Central de Mando:**
- 🗳️: `Producción`
- 🧑‍⚖️: `Abastecimiento`
- 💲: `Costos`
- 🧭: `Turnos`
- 🚥: `Calidad`
""")
st.write("""
**Sistema de Alarmas para:**
- ⏰ : `Retrasos Operativos`
- ⏰ : `Retrasos Temporales`
- ⏰ : `Retrasos Climáticos`
""")
st.write("""
**Sistema de Recomendación para:**
- 📈:  `Más Productividad`
- 📈:  `Más Sostenibilidad`
- 📈:  `Más Rentabilidad`
""")
st.write('---')
st.markdown('Revisa un Prototipo borrador dando click en las secciones de la izquierda 👈')
st.markdown('Conoce todo lo que podemos hacer por ti: www.novussolutions.io')
