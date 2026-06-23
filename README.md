# Pipeline DataOps Gimnasio

## Descripción del proyecto

Este proyecto implementa un pipeline DataOps desarrollado en Python para el procesamiento de datos de asistencia de un gimnasio.

El pipeline permite realizar:

- Ingesta de datos desde archivos CSV
- Procesamiento y transformación de datos
- Validación de calidad
- Generación de KPIs
- Exportación de resultados
- Monitoreo mediante logs

El objetivo es poder automatizar el flujo de procesamiento de datos, al igual que asegurar la calidad e integridad de la información.

# Arquitectura del proyecto
Pipeline-del-banco/
│
├── ingestion/
│   ├── lector_csv.py
│   └── lector_batch.py
│
├── procesamiento/
│   └── transformacion.py
│
├── validacion/
│   └── validar_datos.py
│
├── ia/
│   ├── exploracion.py
│   ├── entrenamiento.py
│   ├── evaluacion.py
│   ├── feature_importance.py
│   └── modelo.pkl
│
├── modelos/
│   ├── modelo_logistico.pkl
│   └── modelo_arbol.pkl
│
├── graficos/
│   ├── matriz_confusion_logistica.png
│   ├── matriz_confusion_arbol.png
│   └── importancia_variables.png
│
├── output/
│   ├── resultado_transformado.csv
│   ├── resumen_clientes.csv
│   ├── kpis.txt
│   └── metricas_modelo.txt
│
├── logs/
│   └── pipeline.log
│
├── pipeline.py
├── Dockerfile
├── requirements.txt
└── README.md

# Tecnologías utilizadas
   Python
   Pandas
   NumPy
   Scikit-learn
   Docker
   Funcionalidades del pipeline

   1. Ingesta de datos
      Se cargan datos desde archivos CSV mediante procesos  batch.

   2. Transformación de datos
      El pipeline realiza:
      Eliminación de duplicados
      Limpieza de valores nulos
      Normalización de edades
      Categorización de edades
      Generación de resúmenes
   
   3. Validación de calidad
      Se validan:
      Valores nulos
      Registros duplicados
      Edades negativas
      Integridad del DataFrame

   4. KPIs del pipeline
      Se generan métricas como:
      Total de registros procesados
      Total de columnas
      Valores nulos
      Registros duplicados
      Porcentaje de completitud
      Tiempo de ejecución

   5. Exportación de resultados

      El pipeline genera automáticamente:
         resultado_transformado.csv
         resumen_clientes.csv
         kpis.txt
         pipeline.log

   6. Modelos de Machine Learning

      Se entrenan dos algoritmos:
         Regresión Logística
         Modelo lineal utilizado para clasificación.
         Árbol de Decisión
         Modelo basado en reglas y estructuras jerárquicas.
         Los modelos entrenados se almacenan en:modelos/modelo_logistico.pkl
         modelos/modelo_arbol.pkl

   7. Evaluación de modelos

      Se calculan las siguientes métricas:

      Accuracy
      Precision
      Recall
      F1-Score
      Classification Report
      Matrices de confusión

   8. Interpretabilidad del modelo

      Se calcula la importancia de las variables mediante:

      "feature_importance.py"
   
   9. Exportación de resultados

      El pipeline genera automáticamente:

      Datos procesados
      resultado_transformado.csv
      resumen_clientes.csv
      Métricas
      kpis.txt
      metricas_modelo.txt
      Modelos entrenados
      modelo_logistico.pkl
      modelo_arbol.pkl
      Gráficos
      matriz_confusion_logistica.png
      matriz_confusion_arbol.png
      importancia_variables.png
      Logs
      pipeline.log

   # Ejecución del proyecto

   Instalar dependencias:
   pip install -r requirements.txt

   Ejecutar el pipeline:
   python pipeline.py

   # Resultado obtenido
   Se entrenaron y compararon dos modelos de Machine Learning:

   Modelo	            Accuracy
   Regresión Logística	73.5 %
   Árbol de Decisión	   98.0 %