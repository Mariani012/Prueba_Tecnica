import os
import pandas as pd


def cargar_archivo_csv():
    """ Read a dataset.
    Read a dataset from the Raw folder.

    Returns:
          Return a data set with the help of the pd library.
    """

    # Ruta al archivo CSV (ajusta la ruta según tu estructura de carpetas)
    ruta_csv = os.path.join(
        "C:/Users/ASUS/PycharmProjects/Prueba/Prueba_Tecnica/ejercicio1/raw/", "data_prueba_tecnica.csv")

    try:
        # Verifica si el archivo existe
        if not os.path.isfile(ruta_csv):
            raise FileNotFoundError(f"El archivo {ruta_csv} no fue encontrado.")
        # Carga el archivo CSV usando pandas
        df = pd.read_csv(ruta_csv)
        return df
    except Exception as e:
        print(f"Error al cargar el archivo CSV: {e}")
        return None


if __name__ == "__main__":
    # Llama a la función para cargar el archivo
    df_dataset = cargar_archivo_csv()
    print(df_dataset.columns)
