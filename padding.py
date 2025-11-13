import streamlit as st

st.title("Padding")
st.write("Kelompok 20")
st.markdown("""
    - FAHLIA ATHIYYA MARWA (0110122176) 
    - FAHMI YUSRON FADILLAH (0110222072)
    - UYUN NILJANAH (0110222081)
 """)

from PIL import Image
img = Image.open("C:\VISUALISASI DATA\praktikum02\Image\payy.png")

col1, padding, col2 = st.columns((10,2,10))
with col1:
    col1.image(img)
with col2:
    col2.image(img)