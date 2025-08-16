def main():
    import streamlit as st

    st.title("DataVisionIA360")
    st.write("Bienvenido al Dashboard interactivo 🚀")

    st.sidebar.header("Menú")
    page = st.sidebar.radio("Selecciona una opción:", ["Inicio", "Dashboard", "Contacto"])

    if page == "Inicio":
        st.write("Aquí estará la descripción de tu consultora.")
    elif page == "Dashboard":
        st.image("dashboard_mockup.png", caption="Vista previa del Dashboard")
    elif page == "Contacto":
        st.write("Correo: elvidi99@gmail.com")
