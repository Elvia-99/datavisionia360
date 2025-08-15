import streamlit as st

def main():
    st.set_page_config(page_title="Dashboard - DataVisionIA360", layout="wide")

    st.title("📊 Dashboard - DataVisionIA360")
    st.markdown("Bienvenido/a al **panel principal** de DataVisionIA360.")

    # Ejemplo de métricas
    col1, col2, col3 = st.columns(3)
    col1.metric("Usuarios activos", "1,245", "+15%")
    col2.metric("Proyectos en curso", "28", "0%")
    col3.metric("Ingresos", "$12,500", "+8%")

    # Ejemplo de gráfico rápido
    import pandas as pd
    import numpy as np

    data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["Ventas", "Costos", "Beneficios"]
    )

    st.line_chart(data)

if __name__ == "__main__":
    main()

