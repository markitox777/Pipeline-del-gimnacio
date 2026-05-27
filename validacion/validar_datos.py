import pandas as pd


def validar_datos(almacen_datos):

    print("\n--- Ejecutando validaciones ---")

    df = almacen_datos["asistencia_gimnasio"]

    errores = []


    #validar si el DataFrame está vacío
    if df.empty:

        errores.append("El DataFrame está vacío.")

    else:

        print("[INFO] El DataFrame contiene registros.")

    #validar datos nulos
    nulos = df.isnull().sum()

    columnas_con_nulos = nulos[nulos > 0]

    if len(columnas_con_nulos) > 0:

        errores.append(
            f"Columnas con valores nulos:\n{columnas_con_nulos}"
        )

    else:

        print("[INFO] No existen valores nulos.")

    #validar edades negativas
    if "edad" in df.columns:

        edades_negativas = df[df["edad"] < 0]

        if len(edades_negativas) > 0:

            errores.append(
                f"Se encontraron {len(edades_negativas)} edades negativas."
            )

        else:

            print("[INFO] No existen edades negativas.")

    #validar datos duplicados
    duplicados = df.duplicated().sum()

    if duplicados > 0:

        errores.append(
            f"Se encontraron {duplicados} registros duplicados."
        )

    else:

        print("[INFO] No existen registros duplicados.")

   #reportar errores encontrados o confirmar que la validación fue exitosa
    if len(errores) > 0:

        print("\n[WARNING] Se encontraron problemas de calidad:")

        for error in errores:

            print(f"- {error}")

    else:

        print("\n[INFO] Validación completada correctamente.")

    return errores