"""### Null treatment"""


def df_statiscal_values(df_dataset, df_columns):
    """ Statistical information for each field.

    Generates statistical information for each field, for example, mode, mean,
    std, median, maximum, minimum.

    Args:
      df_dataset: Dataframe that contains information about payments from different companies .
      df_columns: Dataframe containing the categories to which the fields belong

    Returns:
         A dataframe with the statistical information of each field.
    """
    df_columns['Moda'] = df_columns['Categoría'].map(df_dataset.mode().T[0])
    df_columns['Media'] = df_columns['Categoría'].map(df_dataset.mean())
    df_columns['std'] = df_columns['Categoría'].map(df_dataset.std())
    df_columns['Mediana'] = df_columns['Categoría'].map(df_dataset.median())
    df_columns['Maximo'] = df_columns['Categoría'].map(df_dataset.max())
    df_columns['Minimo'] = df_columns['Categoría'].map(df_dataset.min())
    df_describe_columnas_disc = df_columns[(df_columns['Nulos'] > 0) & (df_columns['Tipo'] == 'Discreta')]
    return (df_describe_columnas_disc[['Categoría', 'Tipo', 'Nulos', 'Porc_nulos',
                                       'Moda', 'Frec_max', 'Porc_frec_max']])
