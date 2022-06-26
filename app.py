!apt apt install figlet -y
from fileinput import filename
import streamlit as st
import os

st.title("Turn Text to Figlet")

text = st.text_input("Enter Text:")

if text:
    os.system(f'figlet -c {text} > figlet.txt')
    st.download_button("Download Figlet", filename="figlet.txt")

