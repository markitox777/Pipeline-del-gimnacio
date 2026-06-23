import matplotlib.pyplot as plt

def importancia_variables(modelo):
    
    importancia = modelo.feature_importances_

    plt.figure(figsize=(6,4))

    plt.bar(
        ["edad_normalizada"],
        importancia
    )

    plt.title("Importancia de variables")
    plt.ylabel("Importancia")

    plt.savefig(
        "graficos/importancia_variables.png"
    )

    plt.close()