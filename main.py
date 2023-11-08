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


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="SanJavierBricks demo Novus", page_icon="🧱")

image = Image.open('SanJavierBricks.jpeg')

st.image(image, caption='Demo Exploratorio 2: Cocción, Curado, Entrenamiento y Turnos. Planta Zamora 🏭')
st.title('Novus - Demo Borrador 2 🧱')



st.title('Centrales de Mando 📈')

st.subheader('Plan de Producción Diario en Planta Zamora🏭')
current_time = time.ctime()
st.write("Siendo HOY y AHORA las: ", current_time)
meta_zona_1 = 10290
meta_zona_2 = 11986
meta_zona_3 = 11368
meta_zona_4 = 14018
meta_zona_5 = 14036
meta_zona_6 = 5241
meta_zona_7 = 3112
meta_zona_8 = 110
meta_zona_9 = 7338
st.header('Ritmo de Producción por turnos para 9 productos')
options = {
            "title": {"text": "Votos x Zonas"},
            "tooltip": {
                "trigger": "axis",
                "axisPointer": {"type": "cross", "label": {"backgroundColor": "#6a7985"}},
            },
            "legend": {"data": ["Producto_9", "Producto_8", "Producto_7", "Producto_6", "Producto_5", "Producto_4", "Producto_3", "Producto_2", "Producto_1"]},
            "toolbox": {"feature": {"saveAsImage": {}}},
            "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
            "xAxis": [
                {
                    "type": "category",
                    "boundaryGap": False,
                    "data": ["00:00", "04:00", "08:00", "12:00", "16:00", "20:00", "23:59"],
                }
            ],
            "yAxis": [{"type": "value"}],
            "series": [
                {
                    "name": "Producto_9",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_9*0.1, meta_zona_9*0.2, meta_zona_9*0.35, meta_zona_9*0.45, meta_zona_9*0.5, meta_zona_9*0.75, meta_zona_9],
                },
                {
                    "name": "Producto_8",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_8*0.1, meta_zona_8*0.2, meta_zona_8*0.35, meta_zona_8*0.45, meta_zona_8*0.5, meta_zona_8*0.75, meta_zona_8],
                },
                {
                    "name": "Producto_7",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_7*0.1, meta_zona_7*0.2, meta_zona_7*0.35, meta_zona_7*0.45, meta_zona_7*0.5, meta_zona_7*0.75, meta_zona_7],
                },
                  {
                    "name": "Producto_6",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_6*0.1, meta_zona_6*0.2, meta_zona_6*0.35, meta_zona_6*0.45, meta_zona_6*0.5, meta_zona_6*0.75, meta_zona_6],
                },
                 {
                    "name": "Producto_5",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_5*0.1, meta_zona_5*0.2, meta_zona_5*0.35, meta_zona_5*0.45, meta_zona_5*0.5, meta_zona_5*0.75, meta_zona_5],
                },
                  {
                    "name": "Producto_4",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_4*0.1, meta_zona_4*0.2, meta_zona_4*0.35, meta_zona_4*0.45, meta_zona_4*0.5, meta_zona_4*0.75, meta_zona_4],
                },
                  {
                    "name": "Producto_3",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_3*0.1, meta_zona_3*0.2, meta_zona_3*0.35, meta_zona_3*0.45, meta_zona_3*0.5, meta_zona_3*0.75, meta_zona_3],
                },
                  {
                    "name": "Producto_2",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_2*0.1, meta_zona_2*0.2, meta_zona_2*0.35, meta_zona_2*0.45, meta_zona_2*0.5, meta_zona_2*0.75, meta_zona_2],
                },
                  {
                    "name": "Producto_1",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_1*0.1, meta_zona_1*0.2, meta_zona_1*0.35, meta_zona_1*0.45, meta_zona_1*0.5, meta_zona_1*0.75, meta_zona_1],
                },
            ],
        }
st_echarts(options=options, height="400px") 

colored_header(
    label="Turnos de Cocción y Curado de Ladrillos",
    description="Tareas por días y horas",
    color_name="violet-70",
)


def render_heatmap_cartesian():
    hours = [
        "12a",
        "1a",
        "2a",
        "3a",
        "4a",
        "5a",
        "6a",
        "7a",
        "8a",
        "9a",
        "10a",
        "11a",
        "12p",
        "1p",
        "2p",
        "3p",
        "4p",
        "5p",
        "6p",
        "7p",
        "8p",
        "9p",
        "10p",
        "11p",
    ]
    days = [
        "Saturday",
        "Friday",
        "Thursday",
        "Wednesday",
        "Tuesday",
        "Monday",
        "Sunday",
    ]

    data = [
        [0, 0, 5],
        [0, 1, 1],
        [0, 2, 0],
        [0, 3, 0],
        [0, 4, 0],
        [0, 5, 0],
        [0, 6, 0],
        [0, 7, 0],
        [0, 8, 0],
        [0, 9, 0],
        [0, 10, 0],
        [0, 11, 2],
        [0, 12, 4],
        [0, 13, 1],
        [0, 14, 1],
        [0, 15, 3],
        [0, 16, 4],
        [0, 17, 6],
        [0, 18, 4],
        [0, 19, 4],
        [0, 20, 3],
        [0, 21, 3],
        [0, 22, 2],
        [0, 23, 5],
        [1, 0, 7],
        [1, 1, 0],
        [1, 2, 0],
        [1, 3, 0],
        [1, 4, 0],
        [1, 5, 0],
        [1, 6, 0],
        [1, 7, 0],
        [1, 8, 0],
        [1, 9, 0],
        [1, 10, 5],
        [1, 11, 2],
        [1, 12, 2],
        [1, 13, 6],
        [1, 14, 9],
        [1, 15, 11],
        [1, 16, 6],
        [1, 17, 7],
        [1, 18, 8],
        [1, 19, 12],
        [1, 20, 5],
        [1, 21, 5],
        [1, 22, 7],
        [1, 23, 2],
        [2, 0, 1],
        [2, 1, 1],
        [2, 2, 0],
        [2, 3, 0],
        [2, 4, 0],
        [2, 5, 0],
        [2, 6, 0],
        [2, 7, 0],
        [2, 8, 0],
        [2, 9, 0],
        [2, 10, 3],
        [2, 11, 2],
        [2, 12, 1],
        [2, 13, 9],
        [2, 14, 8],
        [2, 15, 10],
        [2, 16, 6],
        [2, 17, 5],
        [2, 18, 5],
        [2, 19, 5],
        [2, 20, 7],
        [2, 21, 4],
        [2, 22, 2],
        [2, 23, 4],
        [3, 0, 7],
        [3, 1, 3],
        [3, 2, 0],
        [3, 3, 0],
        [3, 4, 0],
        [3, 5, 0],
        [3, 6, 0],
        [3, 7, 0],
        [3, 8, 1],
        [3, 9, 0],
        [3, 10, 5],
        [3, 11, 4],
        [3, 12, 7],
        [3, 13, 14],
        [3, 14, 13],
        [3, 15, 12],
        [3, 16, 9],
        [3, 17, 5],
        [3, 18, 5],
        [3, 19, 10],
        [3, 20, 6],
        [3, 21, 4],
        [3, 22, 4],
        [3, 23, 1],
        [4, 0, 1],
        [4, 1, 3],
        [4, 2, 0],
        [4, 3, 0],
        [4, 4, 0],
        [4, 5, 1],
        [4, 6, 0],
        [4, 7, 0],
        [4, 8, 0],
        [4, 9, 2],
        [4, 10, 4],
        [4, 11, 4],
        [4, 12, 2],
        [4, 13, 4],
        [4, 14, 4],
        [4, 15, 14],
        [4, 16, 12],
        [4, 17, 1],
        [4, 18, 8],
        [4, 19, 5],
        [4, 20, 3],
        [4, 21, 7],
        [4, 22, 3],
        [4, 23, 0],
        [5, 0, 2],
        [5, 1, 1],
        [5, 2, 0],
        [5, 3, 3],
        [5, 4, 0],
        [5, 5, 0],
        [5, 6, 0],
        [5, 7, 0],
        [5, 8, 2],
        [5, 9, 0],
        [5, 10, 4],
        [5, 11, 1],
        [5, 12, 5],
        [5, 13, 10],
        [5, 14, 5],
        [5, 15, 7],
        [5, 16, 11],
        [5, 17, 6],
        [5, 18, 0],
        [5, 19, 5],
        [5, 20, 3],
        [5, 21, 4],
        [5, 22, 2],
        [5, 23, 0],
        [6, 0, 1],
        [6, 1, 0],
        [6, 2, 0],
        [6, 3, 0],
        [6, 4, 0],
        [6, 5, 0],
        [6, 6, 0],
        [6, 7, 0],
        [6, 8, 0],
        [6, 9, 0],
        [6, 10, 1],
        [6, 11, 0],
        [6, 12, 2],
        [6, 13, 1],
        [6, 14, 3],
        [6, 15, 4],
        [6, 16, 0],
        [6, 17, 0],
        [6, 18, 0],
        [6, 19, 0],
        [6, 20, 1],
        [6, 21, 2],
        [6, 22, 2],
        [6, 23, 6],
    ]
    data = [[d[1], d[0], d[2] if d[2] != 0 else "-"] for d in data]

    option = {
        "tooltip": {"position": "top"},
        "grid": {"height": "50%", "top": "10%"},
        "xAxis": {"type": "category", "data": hours, "splitArea": {"show": True}},
        "yAxis": {"type": "category", "data": days, "splitArea": {"show": True}},
        "visualMap": {
            "min": 0,
            "max": 10,
            "calculable": True,
            "orient": "horizontal",
            "left": "center",
            "bottom": "15%",
        },
        "series": [
            {
                "name": "Punch Card",
                "type": "heatmap",
                "data": data,
                "label": {"show": True},
                "emphasis": {
                    "itemStyle": {"shadowBlur": 10, "shadowColor": "rgba(0, 0, 0, 0.5)"}
                },
            }
        ],
    }
    st_echarts(option, height="500px")


ST_HEATMAP_DEMOS = {
    "Heatmap: Heatmap Cartesian": (
        render_heatmap_cartesian,
        "https://echarts.apache.org/examples/en/editor.html?c=heatmap-cartesian",
    ),
}

render_heatmap_cartesian()


st.subheader('Plan de Abastecimiento')
   
fig1 = go.Figure(data=[go.Sankey(
  node = dict(
    pad = 15,
    thickness = 20,
    line = dict(color = "black", width = 0.5),
    label = ["Fuente1", "Fuente2", "Fuente 3", "Categoría1", "Categoría2", "Producto1"],
    color = "blue"
  ),
  link = dict(
    source = [0, 1, 2, 3, 4], # indices correspond to labels, eg A1, A2, A1, B1, ...
    target = [3, 4, 3, 5, 5],
    value = [8, 4, 5, 13, 4]
))])

fig1.update_layout(title_text="Materias Primas e Insumos", font_size=10)
st.plotly_chart(fig1, theme="streamlit")


    
st.subheader('Control de Calidad')

col1, col2, col3 = st.columns(3)
with col1:
  acelerometro1 = {
        "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
        "series": [
            {
                "name": "Pressure",
                "type": "gauge",
                "axisLine": {
                    "lineStyle": {
                        "width": 10,
                    },
                },
                "progress": {"show": "true", "width": 10},
                "detail": {"valueAnimation": "true", "formatter": "{value}"},
                "data": [{"value": 30, "name": "Humedad"}],
            }
        ],
    }

  st_echarts(options=acelerometro1)

with col2:
  acelerometro2 = {
        "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
        "series": [
            {
                "name": "Pressure",
                "type": "gauge",
                "axisLine": {
                    "lineStyle": {
                        "width": 10,
                    },
                },
                "progress": {"show": "true", "width": 10},
                "detail": {"valueAnimation": "true", "formatter": "{value}"},
                "data": [{"value": 50, "name": "Temperatura"}],
            }
        ],
    }

  st_echarts(options=acelerometro2)

with col3:
  acelerometro3 = {
        "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
        "series": [
            {
                "name": "Pressure",
                "type": "gauge",
                "axisLine": {
                    "lineStyle": {
                        "width": 10,
                    },
                },
                "progress": {"show": "true", "width": 10},
                "detail": {"valueAnimation": "true", "formatter": "{value}"},
                "data": [{"value": 80, "name": "Densidad"}],
            }
        ],
    }
  st_echarts(options=acelerometro3)



st.title('Asistentes Virtuales 🤖 24/7/365 ⏲️')
st.subheader('Entrenamiento')
st.subheader('Cumplimiento Tareas Turnos')




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
