import streamlit as st
import pandas as pd

st.image('Raisin.jpg')
cols1,cols2,cols3=st.columns(3)
with cols1:
with cols2: 
    st.image('Raisin.jpg')
with cols3: 
dt=pd.read_csv('./data/Raisin_Dataset.csv')
html_1 = """
<div style="background-color:#52BE80;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>"ข้อมูลลูกเกต"</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")
st.write(dt.head(7))

html_2 = """
<div style="background-color:#52BE80;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>"สถิติข้อมูลลูกเกต"</h5></center>
</div>
"""
st.markdown(html_2, unsafe_allow_html=True)
st.markdown("")
st.write("ผลรวม")
cl1,cl2,cl3,cl4,cl5,cl6,cl7=st.columns(7)
cl1.write(dt['Area'].sum())
cl2.write(dt['MajorAxisLength'].sum())
cl3.write(dt['MinorAxisLength'].sum())
cl4.write(dt['Eccentricity'].sum())
cl5.write(dt['ConvexArea'].sum())
cl6.write(dt['Extent'].sum())
cl7.write(dt['Perimeter'].sum())