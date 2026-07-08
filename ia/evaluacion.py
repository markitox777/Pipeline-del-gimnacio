import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

Path("graficos").mkdir(exist_ok=True)

from sklearn.preprocessing import label_binarize

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    roc_curve,
    auc
)


def evaluar_modelos(
        modelo_logistico,
        modelo_arbol,
        X_prueba,
        y_prueba):

    # PREDICCIONES

    y_pred_logistico = modelo_logistico.predict(X_prueba)
    y_pred_arbol = modelo_arbol.predict(X_prueba)

    # REGRESIÓN LOGÍSTICA

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

    # MATRIZ DE CONFUSIÓN LOGÍSTICA
    cm_log = confusion_matrix(
        y_prueba,
        y_pred_logistico
    )

    plt.figure(figsize=(7, 6))

    sns.heatmap(
        cm_log,
        annot=True,
        fmt="d",
        cmap="Blues"
    )

    plt.title("Matriz de Confusión - Regresión Logística")
    plt.ylabel("Valor Real")
    plt.xlabel("Predicción")

    plt.savefig("graficos/matriz_logistica.png")

    plt.close()

    # CURVA ROC REGRESIÓN LOGÍSTICA

    y_score_log = modelo_logistico.predict_proba(X_prueba)

    clases_log = modelo_logistico.classes_

    y_bin_log = label_binarize(
        y_prueba,
        classes=clases_log
    )

    fpr_log = {}
    tpr_log = {}
    roc_auc_log = {}

    for i in range(len(clases_log)):

        fpr_log[i], tpr_log[i], _ = roc_curve(
            y_bin_log[:, i],
            y_score_log[:, i]
        )

        roc_auc_log[i] = auc(
            fpr_log[i],
            tpr_log[i]
        )

    auc_promedio_log = sum(
        roc_auc_log.values()
    ) / len(roc_auc_log)

    gini_log = (2 * auc_promedio_log) - 1

    print("\nCURVA ROC - REGRESIÓN LOGÍSTICA")
    print(f"AUC Promedio : {auc_promedio_log:.3f}")
    print(f"Coeficiente Gini : {gini_log:.3f}")

    plt.figure(figsize=(8, 6))

    for i in range(len(clases_log)):

        plt.plot(
            fpr_log[i],
            tpr_log[i],
            label=f"{clases_log[i]} (AUC={roc_auc_log[i]:.2f})"
        )

    plt.plot(
        [0, 1],
        [0, 1],
        "k--"
    )

    plt.title("Curva ROC - Regresión Logística")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.legend()

    plt.savefig("graficos/curva_roc_logistica.png")

    plt.close()

    # ÁRBOL DE DECISIÓN
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

    print("\nÁRBOL DE DECISIÓN")

    print(f"Accuracy : {accuracy_arbol:.3f}")
    print(f"Precision: {precision_arbol:.3f}")
    print(f"Recall   : {recall_arbol:.3f}")
    print(f"F1 Score : {f1_arbol:.3f}")

    print("\nReporte completo Árbol de Decisión:")

    print(
        classification_report(
            y_prueba,
            y_pred_arbol,
            zero_division=0
        )
    )
    

    # MATRIZ DE CONFUSIÓN ÁRBOL
    cm_arbol = confusion_matrix(
        y_prueba,
        y_pred_arbol
    )

    plt.figure(figsize=(7, 6))

    sns.heatmap(
        cm_arbol,
        annot=True,
        fmt="d",
        cmap="Greens"
    )

    plt.title("Matriz de Confusión - Árbol de Decisión")
    plt.ylabel("Valor Real")
    plt.xlabel("Predicción")

    plt.savefig("graficos/matriz_arbol.png")

    plt.close()

    # CURVA ROC ÁRBOL DE DECISIÓN
    y_score_arbol = modelo_arbol.predict_proba(X_prueba)

    clases_arbol = modelo_arbol.classes_

    y_bin_arbol = label_binarize(
        y_prueba,
        classes=clases_arbol
    )

    fpr_arbol = {}
    tpr_arbol = {}
    roc_auc_arbol = {}

    for i in range(len(clases_arbol)):

        fpr_arbol[i], tpr_arbol[i], _ = roc_curve(
            y_bin_arbol[:, i],
            y_score_arbol[:, i]
        )

        roc_auc_arbol[i] = auc(
            fpr_arbol[i],
            tpr_arbol[i]
        )

    auc_promedio_arbol = sum(
        roc_auc_arbol.values()
    ) / len(roc_auc_arbol)

    gini_arbol = (2 * auc_promedio_arbol) - 1

    print("\nCURVA ROC - ÁRBOL DE DECISIÓN")
    print(f"AUC Promedio : {auc_promedio_arbol:.3f}")
    print(f"Coeficiente Gini : {gini_arbol:.3f}")

    plt.figure(figsize=(8, 6))

    for i in range(len(clases_arbol)):

        plt.plot(
            fpr_arbol[i],
            tpr_arbol[i],
            label=f"{clases_arbol[i]} (AUC={roc_auc_arbol[i]:.2f})"
        )

    plt.plot(
        [0, 1],
        [0, 1],
        "k--"
    )

    plt.title("Curva ROC - Árbol de Decisión")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.legend()

    plt.savefig("graficos/curva_roc_arbol.png")

    plt.close()

  
    # COMPARAMOS AMBOS ALGORITMOS
    print("\nCOMPARACIÓN DE MODELOS")

    print(
        f"Accuracy  -> Logística: {accuracy_log:.3f} | Árbol: {accuracy_arbol:.3f}"
    )

    print(
        f"Precision -> Logística: {precision_log:.3f} | Árbol: {precision_arbol:.3f}"
    )

    print(
        f"Recall    -> Logística: {recall_log:.3f} | Árbol: {recall_arbol:.3f}"
    )

    print(
        f"F1 Score  -> Logística: {f1_log:.3f} | Árbol: {f1_arbol:.3f}"
    )

    print(
        f"AUC       -> Logística: {auc_promedio_log:.3f} | Árbol: {auc_promedio_arbol:.3f}"
    )

    print(
        f"Gini      -> Logística: {gini_log:.3f} | Árbol: {gini_arbol:.3f}"
    )

    # MEJOR MODELO
    if accuracy_log > accuracy_arbol:

        print("\n[INFO] El mejor modelo es Regresión Logística.")

    elif accuracy_arbol > accuracy_log:

        print("\n[INFO] El mejor modelo es Árbol de Decisión.")

    else:

        print("\n[INFO] Ambos modelos obtuvieron el mismo Accuracy.")
    
    # EXPORTAR MÉTRICAS
    with open("output/metricas_modelo.txt", "w") as archivo:

        archivo.write("===== REGRESIÓN LOGÍSTICA =====\n")
        archivo.write(f"Accuracy: {accuracy_log:.3f}\n")
        archivo.write(f"Precision: {precision_log:.3f}\n")
        archivo.write(f"Recall: {recall_log:.3f}\n")
        archivo.write(f"F1 Score: {f1_log:.3f}\n")
        archivo.write(f"AUC: {auc_promedio_log:.3f}\n")
        archivo.write(f"Gini: {gini_log:.3f}\n\n")

        archivo.write("===== ÁRBOL DE DECISIÓN =====\n")
        archivo.write(f"Accuracy: {accuracy_arbol:.3f}\n")
        archivo.write(f"Precision: {precision_arbol:.3f}\n")
        archivo.write(f"Recall: {recall_arbol:.3f}\n")
        archivo.write(f"F1 Score: {f1_arbol:.3f}\n")
        archivo.write(f"AUC: {auc_promedio_arbol:.3f}\n")
        archivo.write(f"Gini: {gini_arbol:.3f}\n")

    return {

        "accuracy_log": accuracy_log,
        "precision_log": precision_log,
        "recall_log": recall_log,
        "f1_log": f1_log,
        "auc_log": auc_promedio_log,
        "gini_log": gini_log,

        "accuracy_arbol": accuracy_arbol,
        "precision_arbol": precision_arbol,
        "recall_arbol": recall_arbol,
        "f1_arbol": f1_arbol,
        "auc_arbol": auc_promedio_arbol,
        "gini_arbol": gini_arbol
    }