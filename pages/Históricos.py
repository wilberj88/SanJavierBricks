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

st.title('Central de Datos Históricos - Planta Zamora 🧱')


st.header("Producción Anual por Productos")
options = {
    "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
    "legend": {
        "data": ["2020", "2021", "2022"]
    },
    "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
    "xAxis": {"type": "value"},
    "yAxis": {
        "type": "category",
        "data": ["Cerámica_1", "Cerámica_2", "Cerámica_3", "Cerámica_4", "Cerámica_5", "Cerámica_6", "Cerámica_7", "Cerámica_8", "Cerámica_9"],
    },
    "series": [
        {
            "name": "2020",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [10898, 12260, 10461, 13667, 11792, 4659, 4364, 152, 5931],
        },
        {
            "name": "2021",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [7055, 6004, 5288, 6842, 7077, 4127, 2267, 58, 3337],
        },
        {
            "name": "2022",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [2273, 2792, 2419, 2954, 2437, 974, 916, 16, 2863],
        },
    ],
}
st_echarts(options=options, height="500px")
