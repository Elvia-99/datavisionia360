import pandas as pd

def load_csv(path):
    """
    Carga un archivo CSV y devuelve un DataFrame de Pandas.
    """
    try:
        data = pd.read_csv(path)
        return data
    except Exception as e:
        raise Exception(f"Error cargando el archivo CSV: {e}")

def load_excel(path):
    """
    Carga un archivo Excel y devuelve un DataFrame.
    """
    try:
        data = pd.read_excel(path)
        return data
    except Exception as e:
        raise Exception(f"Error cargando el archivo Excel: {e}")

