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

   plaintext
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
├── output/
│
├── logs/
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