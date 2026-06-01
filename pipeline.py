from ingestion.lector_csv import leer_datos_csv
from ingestion.lector_batch import leer_datos_batch

from procesamiento.transformacion import generar_transformaciones
from validacion.validar_datos import validar_datos

import time
import pandas as pd
from pathlib import Path
import logging

#configuración de logging
logging.basicConfig(
    filename='logs/pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def ejecutar_pipeline():

    print("\nINICIO DEL PIPELINE DATAOPS")
    logging.info("Inicio del pipeline") 
    # Medir tiempo de ejecución
    inicio_pipeline = time.time()

    #dataFrame para almacenar datos transformados
    almacen_datos = {}

   #ingesta CSV

    print("\n Fase 1: Ingesta CSV")

    almacen_datos["asistencia_gimnasio"] = leer_datos_csv()

    print("[INFO] CSV cargado correctamente.")
    logging.info("CSV cargado correctamente")

    #ingesta Batch
    print("\n Fase 2: Ingesta Batch")   
    logging.info("Iniciando ingesta batch")

    almacen_datos["batch"] = leer_datos_batch()

    print("[INFO] Datos batch cargados correctamente.")
    logging.info("Datos batch cargados correctamente.")

    #transformación de datos
    print("\n Fase 3: Transformación de datos")

    almacen_datos = generar_transformaciones(almacen_datos)

    print("[INFO] Transformaciones completadas.")
    logging.info("Transformaciones completadas.")

    #validación de datos
    print("\n[ETAPA 4] Validación")

    errores_validacion = validar_datos(almacen_datos)

    #carga de datos
    df= almacen_datos["asistencia_gimnasio"]
    print("\n Fase 5: Carga de datos")
    logging.info("Iniciando carga de datos")

    output_path = Path("output")

    output_path.mkdir(exist_ok=True)

    archivo_salida = output_path / "resultado_transformado.csv"

    df.to_csv(archivo_salida, index=False)

    print(f"[INFO] Archivo exportado en: {archivo_salida}")
    logging.info(f"Archivo exportado en: {archivo_salida}")

    #agregamos el resumen de clientes por fecha a la carpeta output
    resumen = almacen_datos["Resumen_Clientes"]

    resumen.to_csv(
    output_path / "resumen_clientes.csv"
    )
    #kpis 
    print("\nKPIs DEL PIPELINE")

    df = almacen_datos["asistencia_gimnasio"]

    # KPI 1 - Total registros
    total_registros = len(df)
    print(f"KpI 1 - Total registros: {total_registros}")
    
    # KPI 2 - Total columnas
    total_columnas = len(df.columns)
    print(f"KPI 2 - Total columnas: {total_columnas}")

    # KPI 3 - Valores nulos
    total_nulos = df.isnull().sum().sum()
    print(f"KPI 3 - Total valores nulos: {total_nulos}")

    # KPI 4 - Registros duplicados
    duplicados = df.duplicated().sum()
    print(f"KPI 4 - Registros duplicados: {duplicados}")

    # KPI 5 - Edades negativas
    edades_negativas = len(df[df["edad"] < 0])
    print(f"KPI 5 - Edades negativas: {edades_negativas}")

    # KPI 6 - Porcentaje completitud
    total_celdas = df.shape[0] * df.shape[1]

    completitud = (
        ((total_celdas - total_nulos) / total_celdas) * 100
    )
    print(f"KPI 6 - Porcentaje completitud: {completitud:.2f}%")

    # KPI 7 - Tiempo ejecución
    fin_pipeline = time.time()

    tiempo_ejecucion = fin_pipeline - inicio_pipeline
    print(f"KPI 7 - Tiempo total ejecución: {tiempo_ejecucion:.2f} segundos")

    #kpis agregados a logs
    logging.info(f"Total registros procesados: {total_registros}")
    logging.info(f"Total columnas: {total_columnas}")
    logging.info(f"Valores nulos encontrados: {total_nulos}")

    logging.info(f"Registros duplicados: {duplicados}")
    logging.info(f"Edades negativas detectadas: {edades_negativas}")
    logging.info(f"Porcentaje completitud: {completitud:.2f}%")
    logging.info(f"Tiempo total ejecución: {tiempo_ejecucion:.2f} segundos")

    #mostramos los datos de los kpis
    with open("output/kpis.txt", "w") as archivo:
        archivo.write(f"KPI 1 - Total registros: {total_registros}\n")
        archivo.write(f"KPI 2 - Total columnas: {total_columnas}\n")
        archivo.write(f"KPI 3 - Total valores nulos: {total_nulos}\n")
        archivo.write(f"KPI 4 - Registros duplicados: {duplicados}\n")
        archivo.write(f"KPI 5 - Edades negativas: {edades_negativas}\n")
        archivo.write(f"KPI 6 - Porcentaje completitud: {completitud:.2f}%\n")
        archivo.write(f"KPI 7 - Tiempo total ejecución: {tiempo_ejecucion:.2f} segundos\n")
    return almacen_datos



if __name__ == "__main__":

    ejecutar_pipeline()