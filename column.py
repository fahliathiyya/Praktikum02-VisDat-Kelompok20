import streamlit as st

st.title("Column")
st.write("Kelompok 20")
st.markdown("""
    - FAHLIA ATHIYYA MARWA (0110122176) 
    - FAHMI YUSRON FADILLAH (0110222072)
    - UYUN NILJANAH (0110222081)
 """)

col1, col2 = st.columns(2)

col1.write("Ini adalah kolom pertama")
col1.image("C:\VISUALISASI DATA\praktikum02\Image\Image.jpeg")

col2.write("Ini adalah kolom kedua")
col2.image("C:\VISUALISASI DATA\praktikum02\Image\Tulip.jpg")