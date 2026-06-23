import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

Path("graficos").mkdir(exist_ok=True)

#metricas de evaluación
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
) 

from sklearn.metrics import roc_curve, auc

def evaluar_modelos(
        modelo_logistico,
        modelo_arbol,
        X_prueba,
        y_prueba):
    
    #hacemos predicciones con los modelos entrenados
    y_pred_logistico = modelo_logistico.predict(X_prueba)

    y_pred_arbol = modelo_arbol.predict(X_prueba)

    #calculamos las métricas de evaluación para el modelo de regresión logística
    accuracy_log = accuracy_score(
    y_prueba,
    y_pred_logistico
    )

    precision_log = precision_score(
    y_prueba,
    y_pred_logistico,
    average="weighted",
    zero_division=0
    )

    recall_log = recall_score(
    y_prueba,
    y_pred_logistico,
    average="weighted",
    zero_division=0
    )

    f1_log = f1_score(
    y_prueba,
    y_pred_logistico,
    average="weighted",
    zero_division=0
    )

    print("\nREGRESIÓN LOGÍSTICA")

    print(f"Accuracy : {accuracy_log:.3f}")
    print(f"Precision: {precision_log:.3f}")
    print(f"Recall   : {recall_log:.3f}")
    print(f"F1 Score : {f1_log:.3f}")

    print("\nReporte completo:")

    print(
        classification_report(
            y_prueba,
            y_pred_logistico,
            zero_division=0
        )
    )

    #matriz de confusión para el modelo de regresión logística
    cm = confusion_matrix(
        y_prueba,
        y_pred_logistico
    )

    #graficamos la matriz de confusión para el modelo de regresión logística
    plt.figure(figsize=(7,6))
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues"
    )
    plt.title("Matriz de Confusión")
    plt.ylabel("Valor real")
    plt.xlabel("Predicción")
    
    #guardamos la matriz de confusión del modelo de regresión logística en un archivo
    plt.savefig("graficos/matriz_logistica.png")

    plt.close()
    #modelo de arbol de decisión
    print("\n ARBOL DE DECISIÓN")
    accuracy_arbol = accuracy_score(
    y_prueba,
    y_pred_arbol
    )

    precision_arbol = precision_score(
        y_prueba,
        y_pred_arbol,
        average="weighted",
        zero_division=0
    )

    recall_arbol = recall_score(
        y_prueba,
        y_pred_arbol,
        average="weighted",
        zero_division=0
    )   

    f1_arbol = f1_score(
        y_prueba,
        y_pred_arbol,
        average="weighted",
        zero_division=0
    )
    
    print("\n ARBOL DE DECISIÓN")

    print(f"Accuracy : {accuracy_arbol:.3f}")
    print(f"Precision: {precision_arbol:.3f}")
    print(f"Recall   : {recall_arbol:.3f}")
    print(f"F1 Score : {f1_arbol:.3f}")

    print("\nReporte completo Arbol de Decisión:")

    print(
        classification_report(
            y_prueba,
            y_pred_arbol,
            zero_division=0
        ))
    

    #modelo de arbol de decisión
    cm_arbol = confusion_matrix(
        y_prueba,
        y_pred_arbol
    )

    #graficamos la matriz de confusión para el modelo de arbol de decisión
    plt.figure(figsize=(7, 6))

    sns.heatmap(
        cm_arbol,
        annot=True,
        fmt="d",
        cmap="Greens"
    )

    plt.title("Matriz de Confusión - Árbol de Decisión")
    plt.ylabel("Valor real")
    plt.xlabel("Predicción")

    #guardamos la matriz de confusión del modelo de arbol de decisión en un archivo
    plt.savefig("graficos/matriz_arbol.png")

    plt.close()
    print("\nCOMPARACIÓN DE MODELOS")

    print(f"Accuracy -> Logística:{accuracy_log:.3f} | Árbol:{accuracy_arbol:.3f}")
    print(f"Precision -> Logística:{precision_log:.3f} | Árbol:{precision_arbol:.3f}")
    print(f"Recall -> Logística:{recall_log:.3f} | Árbol:{recall_arbol:.3f}")
    print(f"F1 -> Logística:{f1_log:.3f} | Árbol:{f1_arbol:.3f}")

    #cual es el mejor modelo según el accuracy
    if accuracy_log > accuracy_arbol:
        print("\n[INFO] El mejor modelo es Regresión Logística.")

    elif accuracy_arbol > accuracy_log:
        print("\n[INFO] El mejor modelo es Árbol de Decisión.")

    else:
        print("\n[INFO] Ambos modelos tienen el mismo Accuracy.")

    # EXPORTAR MÉTRICAS
    with open("output/metricas_modelo.txt", "w") as archivo:
        archivo.write(f"Accuracy Logística: {accuracy_log}\n")
        archivo.write(f"Precision Logística: {precision_log}\n")
        archivo.write(f"Recall Logística: {recall_log}\n")
        archivo.write(f"F1 Logística: {f1_log}\n\n")

        archivo.write(f"Accuracy Árbol: {accuracy_arbol}\n")
        archivo.write(f"Precision Árbol: {precision_arbol}\n")
        archivo.write(f"Recall Árbol: {recall_arbol}\n")
        archivo.write(f"F1 Árbol: {f1_arbol}\n")
    
    return {
    "accuracy_log": accuracy_log,
    "precision_log": precision_log,
    "recall_log": recall_log,
    "f1_log": f1_log,
    "accuracy_arbol": accuracy_arbol,
    "precision_arbol": precision_arbol,
    "recall_arbol": recall_arbol,
    "f1_arbol": f1_arbol
    }
