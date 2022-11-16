from asyncore import write
from turtle import title
from unittest import result
import streamlit as st

st.title("Aplikasi rumus luas persegi panjang")

panjang = st.number_input("Masukan Panjang nya",0)
lebar = st.number_input("Masukan Lebar nya jangan lupa",0)
hitung = st.button("Hitung")
rumus = panjang * lebar

if hitung :
    st.success(f"jawaban nya ",rumus)
    st.balloons()