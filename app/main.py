# app/main.py
import streamlit as st
from components.navbar import navbar
from components.sidebar import sidebar

def main():
    st.set_page_config(page_title="DataVisionIA360", page_icon="📊", layout="wide")

    # Barra de navegación superior
    navbar()

    # Menú lateral
    sidebar()

    st.title("🚀 Bienvenido a DataVisionIA360")
    st.markdown("""
    Plataforma integral de **Big Data** e **Inteligencia Artificial** para análisis de negocios.

    ---
    Selecciona una página en el menú lateral para comenzar.
    """)

if __name__ == "__main__":
    main()


