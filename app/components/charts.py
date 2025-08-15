import streamlit as st
import pandas as pd
import numpy as np

def simple_line_chart():
    data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["Ventas", "Costos", "Beneficios"]
    )
    st.line_chart(data)

def simple_bar_chart():
    data = pd.DataFrame({
        "Categoría": ["A", "B", "C", "D"],
        "Valor": [23, 45, 56, 78]
    })
    st.bar_chart(data.set_index("Categoría"))

