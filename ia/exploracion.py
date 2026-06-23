import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def explorar_datos(df):

    print("\nEXPLORACIÓN DE DATOS")

   
    # Información general
    print("\n[INFO] Información general del DataFrame:")
    print(df.info())

    
    # Estadísticas descriptivas
    print("\n[INFO] Estadísticas descriptivas:")
    print(df.describe())

    # Valores nulos
    print("\n[INFO] Valores nulos por columna:")
    print(df.isnull().sum())

    # Distribución de edades (Univariado)
    plt.figure(figsize=(8, 5))

    sns.histplot(
        df["edad"],
        bins=20,
        kde=True
    )
    plt.title("Distribución de edades")
    plt.xlabel("Edad")
    plt.ylabel("Frecuencia")
    plt.show()

    # Distribución de categoria_edad
    print("\n[INFO] Distribución de categoria_edad:")
    print(df["categoria_edad"].value_counts())

    plt.figure(figsize=(8, 5))

    sns.countplot(
        x="categoria_edad",
        data=df
    )

    plt.title("Cantidad de personas por categoría")
    plt.xlabel("Categoría")
    plt.ylabel("Cantidad")

    plt.show()

    # Conversión segura de fecha
    df["fecha"] = pd.to_datetime(
        df["fecha"],
        errors="coerce"
    )

    # Crear día de la semana
    df["dia_semana"] = df["fecha"].dt.day_name()
    
    # Asistencia por día de la semana}
    plt.figure(figsize=(10, 5))

    orden_dias = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    sns.countplot(
        x="dia_semana",
        data=df,
        order=orden_dias
    )

    plt.title("Asistencia por día de la semana")
    plt.xlabel("Día")
    plt.ylabel("Cantidad")

    plt.xticks(rotation=45)

    plt.show()

    # Matriz de correlación
    columnas_numericas = df.select_dtypes(include=["int64", "float64"])

    plt.figure(figsize=(6, 5))

    sns.heatmap(
        columnas_numericas.corr(),
        annot=True,
        cmap="Blues"
    )

    plt.title("Matriz de correlación")

    plt.show()

    print("\n TERMINADA LA EXPLORACIÓN")