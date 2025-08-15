import streamlit as st
from components import navbar, sidebar
from utils import config

# ====== Cargar estilos CSS desde assets/styles.css ======
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ====== Configuración de la página ======
st.set_page_config(
    page_title="DataVisionIA360",
    layout="wide",
    page_icon="assets/logo.png"
)

# ====== Aplicar estilos ======
load_css("assets/styles.css")

# ====== Barra de navegación ======
navbar.render_navbar()

# ====== Barra lateral ======
sidebar.render_sidebar()

# ====== Contenido principal ======
st.title("Bienvenido a DataVisionIA360")
st.write("Tu consultora inteligente en Big Data, IA y Analítica Avanzada.")

# ====== Ejemplo de Dashboard Inicial ======
col1, col2 = st.columns(2)

with col1:
    st.subheader("Vista General")
    st.image("assets/dashboard_mockup.png", caption="Ejemplo de Dashboard", use_column_width=True)

with col2:
    st.subheader("Métricas Clave")
    st.metric(label="Clientes Activos", value="120")
    st.metric(label="Proyectos en Curso", value="15")
    st.metric(label="Satisfacción", value="98%")

st.success("Plataforma lista. Día 1 completado.")

