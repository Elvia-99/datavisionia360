import streamlit as st

def sidebar():
    st.sidebar.title("📂 Navegación")
    menu = st.sidebar.radio("Ir a:", ["Inicio", "Dashboard", "Analytics", "Acerca de"])
    
    if menu == "Inicio":
        st.sidebar.success("Estás en la página principal")
    elif menu == "Dashboard":
        st.sidebar.info("Panel de métricas y visualizaciones")
    elif menu == "Analytics":
        st.sidebar.info("Análisis interactivo de datos")
    elif menu == "Acerca de":
        st.sidebar.info("Información de la plataforma")

