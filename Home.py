import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/377a24ee-4e19-48c9-8a2f-fcada962c70a/oax9riei3m.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello)

st.page_link("Home.py", label="หน้าแรก", icon="🏠")
st.page_link("pages/1🧮 Statistic.py", label="การนำเสนอข้อมูลลูกเกตด้วยสถิติ", icon="1️⃣")
st.page_link("pages/2📊 Chart.py", label="การนำเสนอข้อมูลลูกเกตด้วยจินตทัศน์ข้อมูล", icon="2️⃣", disabled=False)
st.page_link("pages/3🎡 Classsification.py", label="การจำแนกข้อมูลด้วย KNN", icon="2️⃣", disabled=False)
st.page_link("http://www.google.com", label="Google", icon="🌎")