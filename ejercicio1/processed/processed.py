from ejercicio1.helpers.Read import read
from ejercicio1.helpers.Category import category_classification
from ejercicio1.helpers.Missing import missing
from ejercicio1.helpers.Outliers import outliers


def dataset_processed():
    """
    Read a dataset.

    Return:
        A dataframe with the treatment of nulls and outliers to be able to do a proper analysis.
    """

    df_dataset = read.cargar_archivo_csv()
    
    df_columns = category_classification.variables_classifier(df_dataset)
    vard = df_columns[df_columns['Tipo'] == 'Discreta']['Categoría'].to_list()
    varc = df_columns[df_columns['Tipo'] == 'Continua']['Categoría'].to_list()
    tratamiento_disc = "moda"
    processing__nulls_dataset = missing.trat_null_disc(df_dataset, vard, tratamiento_disc)

    dataset = outliers.trat_outliers(processing__nulls_dataset, varc)

    return dataset


if __name__ == "__main__":
    processed_data = dataset_processed()
    print(processed_data)
