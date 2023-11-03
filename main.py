import streamlit as st
from streamlit_extras.let_it_rain import rain 
import folium
import time
import datetime
import pandas as pd
import numpy as np
from PIL import Image


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="SanJavierBricks demo Novus", page_icon="🧱")

image = Image.open('SanJavierBricks.jpeg')

st.image(image, caption='Demo Exploratorio 1')
st.title('SanJavierBricks 🧱 Novus Demo Borrador')



st.title('Cotización Personalizada 🧱 Al instante ⏲️')

st.subheader('Identificación, Tamaño y Financiación')
col1, col2 = st.columns(2)

with col1:
    suits = st.selectbox(
        "Tipo de proyecto?",
        ("Casa", "Piso", "Chalet", "Edificio", "Institución"),
    )
    rooms = st.radio(
        "Cuántos Metros Cuadrados del terreno?",
        options=['1000', '1500','2000', '2500', '3000', '3500', '4000', '4500', '5000'],
    )
    beds = st.selectbox(
        "Cuántos metros cuadrados habilitados para el proyecto?",
        ("250", "500", "750", "1000"),
    )

with col2:
    name = st.text_input('Cuál es el nombre del proyecto?', '''
    ''')
    email = st.text_input('Cuál es tu correo Electrónico?', '''
    ''')
    bank_account =  st.text_input('Número Telefónico?', '''
    ''')
    phone =  st.text_input('Quiénes serán los usuarios del proyecto?', '''
    ''')
    a = st.selectbox('Forma de pago preferida:', ['Efectivo', 'Tarjeta', 'ContraEntrega', 'Cuotas a SanJavierBricks'])

c = st.selectbox('Necesitas financiación?:', ['Yes', 'No'])

b = st.selectbox('Cuota máxima mensual que te puedes permitir?:', ['10.000€', '25.000€', '50.000€', '75.000€', '100.000€'])

d = st.slider('Cuántos años tiene el proyecto?', 0, 24)


st.subheader('Ubicación')
st.write('Selecciona en el mapa el lugar del proveedor más cercano a tu proyecto')
df = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [40.4165, -3.7025],
    columns=['lat', 'lon'])

st.map(df)




st.subheader('Estilo')
st.write('Selecciona el estilo de proyeto de tu mayor interés')

option = st.selectbox(
    'Cuál estilo quieres para tu proyecto?',
    ('Clásico', 'Moderno', 'Ambiental'))
st.write('You selected:', option)

st.subheader('Colores')
st.write('Selecciona la paleta de colores que mejor contraste con tu entorno y clima')
option2 = st.selectbox(
    'Cuál paleta de colores quieres para tu proyecto?',
    ('Oscuros', 'Claros', 'Grises'))
st.write('You selected:', option2)


st.subheader('Acesorios')
st.write('Selecciona los complementos que embellezcan y aumenten la vida útil de tu proyecto')
option3 = st.selectbox(
    'Cuáles accesorios quieres para tu proyecto?',
    ('Canelones', 'Páneles', 'Sensores'))
st.write('You selected:', option3)






h = st.button('Crear Tu Cotización de SanJavierBricks 🧱 YA')

if h:
    rain(
        emoji="🎈",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )
    st.write('¡Tu cotización ha sido enviada a tu correo')
    st.header("Diagnóstico de tu necesidad y riesgos climáticos")
    st.subheader('Necesitas para tu proyecto')
    col5, col6, col7, col8 = st.columns(4)
    col5.metric("Ladrillos unitarios", "132457", "14%")
    col6.metric("Termoceratres", "10456", "-18%")
    col7.metric("Bovedilla", "2", "13%")
    col8.metric("Klinker", "7", "18%")
    st.subheader('Nuestra cotización ha sido personalizada a tus riesgos climáticos:')
    current_time = time.ctime()
    st.write("At: ", current_time)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Incendios", "57%", "14%")
    col2.metric("Derrumbes", "25%", "-18%")
    col3.metric("Inundaciones", "89%", "13%")
    col4.metric("Huracanes", "45%", "18%")


st.write('---')
st.title('Gemelos Digitales')
st.subheader(':yellow[Productos, Servicios, Procesos y Personal]👤')

st.title('Servicios Web')
st.subheader(':red[Venta Personalizada, Gestión Trabajadores, Mandos, Atentos] 🎯')

st.title('MANDOS')
st.subheader(':red[Productos, Ventas, Inventario, Trabajadores, Proveedores, Tendencias] 🎯')

st.title('ATENTOS')
st.subheader(':blue[Bienvenida con Cotización Personalizada, Atención al Cliente Personalizada ]👤')

st.write('---')
