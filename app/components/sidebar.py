import streamlit as st

def render_sidebar():
    st.sidebar.title("📂 Navegación")
    choice = st.sidebar.radio(
        "Ir a:",
        ["Inicio", "Dashboard", "Analytics", "Acerca de", "DB Test"]
    )
    return choice
