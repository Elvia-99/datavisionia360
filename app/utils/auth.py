import streamlit as st

def login():
    """
    Simula un inicio de sesión simple con nombre de usuario y contraseña.
    """
    st.sidebar.subheader("🔐 Inicio de Sesión")
    username = st.sidebar.text_input("Usuario")
    password = st.sidebar.text_input("Contraseña", type="password")

    if st.sidebar.button("Iniciar sesión"):
        if username == "admin" and password == "1234":
            st.session_state["logged_in"] = True
            st.sidebar.success("✅ Sesión iniciada")
        else:
            st.sidebar.error("❌ Usuario o contraseña incorrectos")

def check_login():
    """
    Verifica si el usuario ha iniciado sesión.
    """
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

