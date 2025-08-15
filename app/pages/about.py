import streamlit as st

def main():
    st.set_page_config(page_title="Acerca de - DataVisionIA360", layout="wide")

    st.title("ℹ️ Acerca de DataVisionIA360")
    st.markdown("""
    **DataVisionIA360** es una plataforma de análisis y visualización de datos en tiempo real.  
    Diseñada para empresas que buscan **tomar decisiones basadas en datos**, combinando **Big Data**,  
    **Inteligencia Artificial** y **análisis interactivo**.

    ---
    **Funciones principales:**
    - Dashboards en tiempo real
    - Integración con múltiples fuentes de datos
    - Análisis predictivo con IA
    - Reportes automáticos
    """)

    st.info("Versión 1.0 - Proyecto en desarrollo")

if __name__ == "__main__":
    main()

