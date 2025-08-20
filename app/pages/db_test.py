import streamlit as st
import pandas as pd
from utils.db import insert_lead, get_leads

def render():
    st.header("🔌 Prueba de conexión a Supabase")

    with st.form("lead_form", clear_on_submit=True):
        name = st.text_input("Nombre")
        email = st.text_input("Email")
        source = st.selectbox("Fuente", ["web", "landing", "referido", "otro"])
        submitted = st.form_submit_button("Guardar en BD")

    if submitted:
        if not name or not email:
            st.warning("Completa nombre y email.")
        else:
            try:
                insert_lead(name, email, source)
                st.success("✅ Registro guardado en Supabase")
            except Exception as e:
                st.error(f"❌ Error al insertar: {e}")

    st.subheader("📋 Leads recientes")
    try:
        rows = get_leads(50)
        if rows:
            st.dataframe(pd.DataFrame(rows))
        else:
            st.info("Aún no hay registros.")
    except Exception as e:
        st.error(f"No se pudo leer: {e}")
