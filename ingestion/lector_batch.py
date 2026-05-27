import pandas as pd
from pathlib import Path

def leer_datos_batch(ruta_archivo="asistencia_gimnasio.csv"):
    source = Path(__file__).resolve().parents[1] / ruta_archivo
    df = pd.read_csv(source)

    columnas_clave = ["fecha","hora","nombre","apellido","edad"]
    df_filtrado = df[columnas_clave]

    print(f"Batch procesó {len(df_filtrado)} registros del gimnasio.")
    return df_filtrado

if __name__ == "__main__":
    df_batch = leer_datos_batch()
    print(df_batch.head())