import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)


with col1:
    st.image("Images/Rajaa C.jpg")

with col2:
    st.header("Rajaa Chandramohan")
    content="""I'm an aspiring Machine Learning developer with a Bachelor's in Engineering and a PG Diploma in AI & ML.
    I'm looking to advance my career by constantly learning and implementing new ideas and technologies."""
    st.write(content)

content2="""Below you can find some of the apps I have built in Python. 
Feel free to contact me!"""
st.info(content2)

data = pd.read_csv("data1.csv", sep=';')

col3, dupl_col, col4 = st.columns([1.5,0.5,1.5])

with col3:
    for index, rows in data[:10].iterrows():
        title=rows['title']
        st.subheader(title)
        st.image("Images/" + rows['image'])
        st.write(rows['description'])
        st.write(f"[source code]({rows['url']})")


with col4:
    for index, rows in data[10:].iterrows():
        st.subheader(rows['title'])
        st.image("Images/" + rows['image'])
        st.write(rows['description'])
        st.write(f"[source code]({rows['url']})")