import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def generar_transformaciones(almacen_datos):

    print("\n--- Ejecutando transformaciones ---")

    # Obtener DataFrame desde el diccionario
    df = almacen_datos["asistencia_gimnasio"].copy()

    
    Datos_antes = len(df)

    #eliminar duplicados
    df = df.drop_duplicates()

    Datos_despues = len(df)

    print(f"[INFO] Duplicados eliminados: {Datos_antes - Datos_despues}")


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
    

    # Eliminar nulos 
    df = df.dropna(subset=columnas_obligatorias)

    print(f"[INFO] Filas restantes después de limpieza: {len(df)}")

    if "edad" in df.columns:

        scaler = MinMaxScaler()

        # Convertir a numérico
        df["edad"] = pd.to_numeric(df["edad"], errors="coerce")

        # Rellenar nulos con mediana
        df["edad"] = df["edad"].fillna(df["edad"].median())

        # Normalización 0-1
        df["edad_normalizada"] = scaler.fit_transform(df[["edad"]])

        print("[INFO] Columna 'edad_normalizada' creada.")

    # =========================
    # 4. CREACIÓN DE CATEGORÍAS
    # =========================

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

    # =========================
    # 5. RESUMEN POR FECHA
    # =========================

    resumen_clientes = df.groupby("fecha").size()

    almacen_datos["Resumen_Clientes"] = resumen_clientes

    print("[INFO] Resumen de clientes por fecha generado.")

    # =========================
    # 6. VALIDACIÓN BÁSICA
    # =========================

    edades_invalidas = df[df["edad"] < 0]

    if len(edades_invalidas) > 0:

        print("[WARNING] Existen edades negativas.")

    else:

        print("[INFO] Validación de edades completada correctamente.")

    # =========================
    # 7. GUARDAR DATAFRAME
    # =========================

    almacen_datos["asistencia_gimnasio"] = df

    print("[INFO] Transformaciones finalizadas correctamente.")

    return almacen_datos