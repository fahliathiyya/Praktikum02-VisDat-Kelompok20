import streamlit as st

st.title("Grid")
st.write("Kelompok 20")
st.markdown("""
    - FAHLIA ATHIYYA MARWA (0110122176) 
    - FAHMI YUSRON FADILLAH (0110222072)
    - UYUN NILJANAH (0110222081)
 """)

from PIL import Image
img = Image.open("C:\VISUALISASI DATA\praktikum02\Image\Anggrek.png")

for a in range(4):
    cols = st.columns((1, 1, 1, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)