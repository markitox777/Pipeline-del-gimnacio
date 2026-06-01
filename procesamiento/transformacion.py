import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import logging


def generar_transformaciones(almacen_datos):

    print("\n--- Ejecutando transformaciones ---")
    logging.info("Ejecutando transformaciones")

    # Obtener DataFrame desde el diccionario
    df = almacen_datos["asistencia_gimnasio"].copy()

    
    Datos_antes = len(df)

    #eliminar duplicados
    df = df.drop_duplicates()

    Datos_despues = len(df)

    print(f"[INFO] Duplicados eliminados: {Datos_antes - Datos_despues}")
    logging.info(f"Duplicados eliminados: {Datos_antes - Datos_despues}")


    # Columnas de los datos
    columnas_obligatorias = [
        "nombre",
        "apellido",
        "edad",
        "fecha",
        "hora"
    ]

    # valores nulos
    nulos = df[columnas_obligatorias].isnull().sum()

    print(f"\n[INFO] Valores nulos encontrados: {nulos.sum()}")
    logging.info(f"Valores nulos encontrados: {nulos.sum()}")
    

    #normalizar fechas
    if "fecha" in df.columns:

    # Convertir múltiples formatos automáticamente
        df["fecha"] = pd.to_datetime(
            df["fecha"],
            errors="coerce",
            dayfirst=True
        )
    
    fechas_invalidas = df["fecha"].isnull().sum()

    print(f"Fechas inválidas detectadas: {fechas_invalidas}")
    logging.info(f"Fechas inválidas detectadas: {fechas_invalidas}")

    # transformar la fecha al formato YYYY-MM-DD
    df["fecha"] = df["fecha"].dt.strftime("%Y-%m-%d")

    print("[INFO] Fechas cambiadas correctamente.")
    logging.info("Fechas cambiadas correctamente.")
    

    # Eliminar nulos 
    df = df.dropna(subset=columnas_obligatorias)

    print(f"[INFO] Filas restantes después de limpieza: {len(df)}")
    logging.info(f"Filas restantes después de limpieza: {len(df)}")

    if "edad" in df.columns:

        scaler = MinMaxScaler()

        # Convertir a numérico
        df["edad"] = pd.to_numeric(df["edad"], errors="coerce")

        # Rellenar nulos con mediana
        df["edad"] = df["edad"].fillna(df["edad"].median())

        # Normalización 0-1
        df["edad_normalizada"] = scaler.fit_transform(df[["edad"]])
        df["edad_normalizada"] = df["edad_normalizada"].round(2)

        print("[INFO] Columna 'edad_normalizada' creada.")
        logging.info("Columna 'edad_normalizada' creada.")

    #creacion de categorias de edad
    def categorizar_edad(edad):

        if edad < 18:
            return "Menor de edad"

        elif edad <= 30:
            return "Joven"

        elif edad <= 50:
            return "Adulto"

        else:
            return "Adulto mayor"

    df["categoria_edad"] = df["edad"].apply(categorizar_edad)

    print("[INFO] Columna 'categoria_edad' creada.")
    logging.info("Columna 'categoria_edad' creada.")

    #resumen de clientes por fecha
    resumen_clientes = df.groupby("fecha").size()

    almacen_datos["Resumen_Clientes"] = resumen_clientes

    print("[INFO] Resumen de clientes por fecha generado.")
    logging.info("Resumen de clientes por fecha generado.")

    #validación de edades negativas
    edades_invalidas = df[df["edad"] < 0]

    if len(edades_invalidas) > 0:

        print("[WARNING] Existen edades negativas.")
        logging.warning("Existen edades negativas.")
    else:

        print("[INFO] Validación de edades completada correctamente.")
        logging.info("Validación de edades completada correctamente.")

    # Actualizar el DataFrame transformado en el diccionario
    almacen_datos["asistencia_gimnasio"] = df

    print("[INFO] Transformaciones finalizadas correctamente.")
    logging.info("Transformaciones finalizadas correctamente.")

    return almacen_datos