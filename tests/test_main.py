import pytest
import streamlit as st
from main import main

def test_main_runs(monkeypatch):
    """Verifica que la función principal se ejecute sin errores."""
    try:
        # Usamos monkeypatch para evitar bloqueos de Streamlit en test
        monkeypatch.setattr(st, 'write', lambda x: None)
        main()
    except Exception as e:
        pytest.fail(f"main() lanzó una excepción: {e}")

