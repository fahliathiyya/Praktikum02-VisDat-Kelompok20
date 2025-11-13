import streamlit as st
import numpy as np

st.title("Container")
st.write("Kelompok 20")
st.markdown("""
    - FAHLIA ATHIYYA MARWA (0110122176) 
    - FAHMI YUSRON FADILLAH (0110222072)
    - UYUN NILJANAH (0110222081)
 """)

with st.container():
    st.write("Element Inside Container")
    # Defining Chart Element
    st.line_chart(np.random.randn(40, 4))
    st.write("Element Outside Container")

st.title("Out of Order Container")
# Defining Containers
container_one = st.container()
container_one.write("Element One Inside Container")
st.write("Element Outside Container")

container_one.write("Element Two Inside Container")
container_one.line_chart(np.random.randn(40, 4))