import streamlit as st

st.title("Sidebar")
st.write("Kelompok 20")
st.markdown("""
    - FAHLIA ATHIYYA MARWA (0110122176) 
    - FAHMI YUSRON FADILLAH (0110222072)
    - UYUN NILJANAH (0110222081)
 """)

st.sidebar.title("Sidebar")
st.sidebar.radio("Are You a New User", ["Yes", "No"])
st.sidebar.slider("Select a Number", 0,10)