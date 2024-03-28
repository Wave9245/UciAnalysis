import pandas as pd
st.subheader(".data/Raisin_Dataset.csv")
st.write(df.head(10))

st.subheader("สถิติข้อมูลลูกเกต")
st.write("ผลรวม")
cl1,cl2,cl3,cl4,cl5,cl6,cl7=st.columns(7)
cl1.write(dt['Area'].sum())
cl2.write(dt['MajorAxisLength'].sum())
cl3.write(dt['MinorAxisLength'].sum())
cl4.write(dt['Eccentricity'].sum())
cl5.write(dt['ConvexArea'].sum())
cl6.write(dt['Extent'].sum())
cl7.write(dt['Perimeter'].sum())