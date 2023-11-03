import streamlit as st
from streamlit_extras.let_it_rain import rain 

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="SanJavierBricks demo Novus", page_icon="🧱")

st.title('SanJavierBricks 🧱 Novus Demo')

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

st.title('Demo Cotización Personalizada 🧱 Al instante ⏲️')

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
st.write('Selecciona en el mapa el lugar de tu proyecto')

st.subheader('Estilo')
st.write('Selecciona el estilo de proyeto de tu mayor interés')


st.subheader('Colores')
st.write('Selecciona la paleta de colores que mejor contraste con tu entorno y clima')


st.subheader('Acesorios')
st.write('Selecciona los complementos que embellezcan y aumenten la vida útil de tu proyecto')






h = st.button('Crear Tu Cotización de SanJavierBricks 🧱 YA')

if h:
    rain(
        emoji="🎈",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )
    st.write('¡Tu cotización ha sido enviada a tu correo')

