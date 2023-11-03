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

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="MANDOS Novus Hotel", page_icon="🛏️")

st.title('MANDOS 🛏️ Novus Hotel')
current_time = time.ctime()
st.write("In real time monitoring at: ", current_time)


st.header('Operation')
colored_header(
    label="Key Performance Indicators",
    description="Plans, Tasks & Results",
    color_name="violet-70",
)
topic = st.selectbox("Choose Topic to Monitor:",
        ("Suits", "Rooms", "Beds", "Staff", "Expenditures", "Savings", "Profits"),
    )

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
                "data": [{"value": 85, "name": "Reservations"}],
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
                "data": [{"value": 70, "name": "Ocupation"}],
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
                "data": [{"value": 100, "name": "Cleaning"}],
            }
        ],
    }
  st_echarts(options=acelerometro3)

colored_header(
    label="Commercial Insights",
    description="Temporal, Climatological & Inflation warnings of danger",
    color_name="red-70",
)

#ALARMS CONFIGURATION
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "146090ad17fa8843bc9eca97c53926b4"
sity1 = "New York"
sity2 = "Amsterdam"
URL1 = BASE_URL + "q=" + sity1 + "&appid=" + API_KEY
URL2 = BASE_URL + "q=" + sity2 + "&appid=" + API_KEY
response1 = requests.get(URL1)
response2 = requests.get(URL2)

if response1.status_code == 200:
   # getting data in the json format
   data1 = response1.json()
   # getting the main dict block
   main1 = data1['main']
  # getting temperature
   temperature1 = main1['temp']
   # getting the humidity
   humidity1 = main1['humidity']
   # getting the pressure
   pressure1 = main1['pressure']
   # weather report
   report1 = data1['weather']

if response2.status_code == 200:
   # getting data in the json format
   data2 = response2.json()
   # getting the main dict block
   main2 = data2['main']
  # getting temperature
   temperature2 = main2['temp']
   # getting the humidity
   humidity2 = main2['humidity']
   # getting the pressure
   pressure2 = main2['pressure']
   # weather report
   report2 = data2['weather']

pytrends = TrendReq(hl='en-US', tz=360)
col4, col5, col6 = st.columns(3)

with col4:
    st.write("🇺🇸 Top10 Trending Search in last hour")
    # Google Trends data
    df1 = pytrends.trending_searches(pn='united_states')
    st.dataframe(df1.head(10))

with col5:
    st.write("🌧 Climate Right Now")
    st.write(f"{sity1:-^30}")
    st.write(f"Temperature (Kelvins): {temperature1}")
    st.write(f"Humidity: {humidity1}")
    st.write(f"Pressure: {pressure1}")
    st.write(f"Weather Report: {report1[0]['description']}")
    st.write(f"{sity2:-^30}")
    st.write(f"Temperature (Kelvins): {temperature2}")
    st.write(f"Humidity: {humidity2}")
    st.write(f"Pressure: {pressure2}")
    st.write(f"Weather Report: {report2[0]['description']}")
    
with col6:
    st.write('💲 Proyected Inflation in 12 months')
    col6.metric("Aliments", "21%", "13%")
    col6.metric("Raw Materials", "16%", "5%")
    col6.metric("Staff", "15%", "3%")
    col6.metric("General", "17%", "3%")
    


colored_header(
    label="Sales Recommendations",
    description="Adds, Speech & Price suggestions",
    color_name="blue-70",
)
col7, col8, col9 = st.columns(3)

with col7:
    st.write('📢 Where to Advertise')
    option = {
        "legend": {},
        "tooltip": {"trigger": "axis", "showContent": False},
        "dataset": {
            "source": [
                ["product", "Monday", "Thursday", "Wednesday", "Tuesday", "Friday", "Saturday"],
                ["TikTok", 56.5, 82.1, 88.7, 70.1, 53.4, 85.1],
                ["Facebook & IG", 51.1, 51.4, 55.1, 53.3, 73.8, 68.7],
                ["Google & Youtube", 40.1, 62.2, 69.5, 36.4, 45.2, 32.5],
                ["Emailing", 25.2, 37.1, 41.2, 18, 33.9, 49.1],
            ]
        },
        "xAxis": {"type": "category"},
        "yAxis": {"gridIndex": 0},
        "grid": {"top": "55%"},
        "series": [
            {
                "type": "line",
                "smooth": True,
                "seriesLayoutBy": "row",
                "emphasis": {"focus": "series"},
            },
            {
                "type": "line",
                "smooth": True,
                "seriesLayoutBy": "row",
                "emphasis": {"focus": "series"},
            },
            {
                "type": "line",
                "smooth": True,
                "seriesLayoutBy": "row",
                "emphasis": {"focus": "series"},
            },
            {
                "type": "line",
                "smooth": True,
                "seriesLayoutBy": "row",
                "emphasis": {"focus": "series"},
            },
            {
                "type": "pie",
                "id": "pie",
                "radius": "30%",
                "center": ["50%", "25%"],
                "emphasis": {"focus": "data"},
                "label": {"formatter": "{b}: {@2012} ({d}%)"},
                "encode": {"itemName": "product", "value": "Monday", "tooltip": "Monday"},
            },
        ],
    }
    st_echarts(option, height="500px", key="echarts")
    
with col8:
    st.write('🌹 Speech to Persuade NOW')
    with st.expander("About Yesterday:"):
        st.subheader('For Womens')
        st.write('Yesterday the rain could´t stopped you. Today you could everything. Visit Novus Hotel 🛏️')
        st.subheader('For Mens')
        st.write('You miss the sun of yesterday as you miss your exgirlfriend. Forget all. Visit Novus Hotel 🛏️')
        
    with st.expander("About Today:"):
        st.subheader('For Womens')
        st.write('Even rain can´t stop you. Come here. Visit Novus Hotel 🛏️')
        st.subheader('For Mens')
        st.write('Don´t let the rain stop you. Come here. Visit Novus Hotel 🛏️')
        
    with st.expander("About Tomorrow:"):
        st.subheader('For Womens')
        st.write('Come to Novus Hotel 🛏️ and sing with us tomorrow about fridays life in our Karaoke Room')
        st.subheader('For Mens')
        st.write('Save 30% reserving today your suit for tomorrow. Just do it now. Reserve Novus Hotel 🛏️')


with col9:
    st.write('💰 Price Suggestions')
    with st.expander("TODAY:"):
        st.subheader('Suits')
        st.write('1000€ per day')
        st.subheader('Rooms')
        st.write('500€ per day')
        st.subheader('Beds')
        st.write('250€ per day')
    with st.expander("TOMORROW:"):
        st.subheader('Suits')
        st.write('1500€ per day')
        st.subheader('Rooms')
        st.write('600€ per day')
        st.subheader('Beds')
        st.write('350€ per day')
    with st.expander("NEXT WEEK:"):
        st.subheader('Suits')
        st.write('900€ per day')
        st.subheader('Rooms')
        st.write('400€ per day')
        st.subheader('Beds')
        st.write('200€ per day')
