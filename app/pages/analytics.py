import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.set_page_config(page_title="Analytics - DataVisionIA360", layout="wide")

    st.title("📈 Análisis de Datos")
    st.markdown("Aquí puedes **explorar y analizar datos** en tiempo real.")

    # Ejemplo de datos
    df = pd.DataFrame(
        np.random.randn(50, 3),
        columns=["Métrica A", "Métrica B", "Métrica C"]
    )

    st.dataframe(df)

    # Filtro interactivo
    filtro = st.slider("Selecciona un valor mínimo para Métrica A", min_value=float(df["Métrica A"].min()), max_value=float(df["Métrica A"].max()), step=0.1)
    df_filtrado = df[df["Métrica A"] >= filtro]
    st.write("Datos filtrados:")
    st.dataframe(df_filtrado)

if __name__ == "__main__":
    main()

