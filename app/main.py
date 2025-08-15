# app/main.py
import streamlit as st

def main():
    st.set_page_config(page_title="DataVisionIA360", page_icon="📊", layout="wide")
    st.title("🚀 Bienvenido a DataVisionIA360")
    st.markdown("""
    Plataforma de Inteligencia de Negocios y Big Data.
    
    Usa el menú de la izquierda para navegar entre las páginas disponibles.
    """)
    st.info("Esta es la versión inicial conectada a Streamlit Cloud.")

if __name__ == "__main__":
    main()

