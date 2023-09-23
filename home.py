import streamlit as st

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
st.write(content2)
