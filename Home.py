import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/ca730b3b-9cc3-43f1-9e07-b6969e78f6b2/nZma1dmZLC.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello)

st.subheader("การประยุกต์ใช้งาน Manchine Learning บนเว็บ")
st.subheader("by วรเมธ กายจะโป๊ะ")
st.subheader("สาขาวิทยาการคอมพิวเตอร์")
st.subheader("คณะวิทยาศาสตร์และเทคโนโลยี")
st.subheader("มหาวิทยาลัยราชภัฏนครปฐม")

st.page_link("Home.py", label="หน้าแรก", icon="🏠")
st.page_link("pages/1🧮 Statistic.py", label="การนำเสนอข้อมูลลูกเกตด้วยสถิติ", icon="1️⃣")
st.page_link("pages/2📊 Chart.py", label="การนำเสนอข้อมูลลูกเกตด้วยจินตทัศน์ข้อมูล", icon="2️⃣", disabled=False)
st.page_link("pages/3🎡 KNNClasssifi.py", label="การจำแนกข้อมูลด้วยเทคนิคKNN", icon="3️⃣", disabled=False)
st.page_link("pages/4🌳 Decisiontree.py", label="การจำแนกข้อมูลด้วยเทคนิคDecisiontree", icon="4️⃣", disabled=False)
st.page_link("pages/5📩 NaivegayeClassify.py", label="การจำแนกข้อมูลด้วยเทคนิคNaiveBayes", icon="5️⃣", disabled=False)
st.page_link("pages/6📈 RegressionOrediction.py", label="การจำแนกข้อมูลด้วยเทคนิคRegression", icon="4️5️6️⃣", disabled=False)
st.page_link("http://www.google.com", label="Google", icon="🌎")