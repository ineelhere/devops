import streamlit as st
import os

st.title("Turn Text to Figlet")

text = st.text_input("Enter Text:")

if text:
    os.system(f'figlet -c {text} > figlet.txt')
    st.text(open('figlet.txt', 'r').read())

st.markdown("""
___
[@ineelhere](https://github.com/ineelhere/)
""", unsafe_allow_html=True)