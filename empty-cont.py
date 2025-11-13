import streamlit as st
import time

st.title("Empty Containers")
st.write("Kelompok 20")
st.markdown("""
    - FAHLIA ATHIYYA MARWA (0110122176) 
    - FAHMI YUSRON FADILLAH (0110222072)
    - UYUN NILJANAH (0110222081)
 """)

with st.empty():
    for seconds in range(5):
        st.write(f" {seconds} seconds have passed")
        time.sleep(1)
        st.write(" Time up!")