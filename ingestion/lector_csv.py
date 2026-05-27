import pandas as pd
from pathlib import Path

def leer_datos_csv():
    try: 
        source = Path(__file__).resolve().parents[1] / "asistencia_gimnasio.csv"
        df = pd.read_csv(source)
        print(f'total lineas importadas:  {len(df)}')
        
        return df
    except Exception as e:
        print(f"Error Archivo csv no se encuentra: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    leer_datos_csv()