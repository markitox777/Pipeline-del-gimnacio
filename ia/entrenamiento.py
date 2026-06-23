import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

import joblib


def entrenar_modelos(df):

    # Variable objetivo
    y = df["categoria_edad"]

    # Variables predictoras
    X = df[["edad_normalizada"]]

    print("\n[INFO] Variables seleccionadas")
    print("X:")
    print(X.head())

    print("\ny:")
    print(y.head())

    # División entrenamiento/prueba
    X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    #modelo 1: Regresión Logística
    modelo_logistico = LogisticRegression(
        max_iter=100,
        random_state=42
    )

    modelo_logistico.fit(
        X_entrenamiento,
        y_entrenamiento
    )

    print("[INFO] Regresión Logística entrenada.")

    #modelo 2: Árbol de Decisión
    modelo_arbol = DecisionTreeClassifier(
        max_depth=5,
        random_state=42
    )

    modelo_arbol.fit(
        X_entrenamiento,
        y_entrenamiento
    )

    print("[INFO] Árbol de Decisión entrenado.")

    # Guardar los modelos entrenados
    Path("modelos").mkdir(exist_ok=True)

    joblib.dump(
        modelo_logistico,
        "modelos/modelo_logistico.pkl"
    )

    joblib.dump(
        modelo_arbol,
        "modelos/modelo_arbol.pkl"
    )

    print("[INFO] Modelos guardados correctamente.")

    #retornar los modelos y los conjuntos de prueba para evaluación
    return {
        "modelo_logistico": modelo_logistico,
        "modelo_arbol": modelo_arbol,
        "X_test": X_prueba,
        "y_test": y_prueba
    }