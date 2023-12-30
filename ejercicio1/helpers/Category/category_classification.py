import pandas as pd


def variables_classifier(df_dataset, porc_nulos=.5, porc_lim_unitario=.75,
                         porc_unique_text=.20, porc_unique_num=.01):
    """ Field analysis description.

    Analyze by field the number of nulls, type of data it contains, unique values,
    maximum frequency to know which category the field corresponds to.

    Args:
        df_dataset: Data set being analyzed.
        porc_nulos: Limit to classify a 'Nula' category field.
        porc_lim_unitario: Limit to classify a 'Unitaria' category field.
        porc_unique_text: Limit to classify a 'Discreta' category field.
        porc_unique_num: Limit to classify a 'Discreta' category field.

    Returns:
         A dataframe with the category that corresponds to each field.
         example:
         if porc_nulos >= .5 then category field is 'Nula'
         if porc_lim_unitario >= .75 then category field is 'Unitaria'
         if porc_unique_text < .20 then category field is 'Discreta'
         if porc_unique_num < .01 then category field is 'Discreta'
    """

    variables = df_dataset.columns.to_list()
    df_columns = pd.DataFrame(variables, columns=['Categoría'])
    df_columns['Type'] = df_columns['Categoría'].map(df_dataset.dtypes)
    df_columns['Count'] = df_columns['Categoría'].map(df_dataset.count())
    df_columns['Nulos'] = df_columns['Categoría'].map(df_dataset.shape[0] - df_dataset.count())
    df_columns['Porc_nulos'] = df_columns['Nulos'] / df_dataset.shape[0]
    df_columns['Unique'] = df_columns['Categoría'].map(df_dataset.nunique())
    df_columns['Porc_unique'] = df_columns['Unique'] / df_dataset.shape[0]

    maxi = []
    for i in variables:
        maxi.append(df_dataset[i].value_counts().to_list()[0])
    df_columns['Frec_max'] = maxi
    df_columns['Porc_frec_max'] = df_columns['Frec_max'] / df_dataset.shape[0]

    # Clasificación
    tipos = []
    for i in range(df_columns.shape[0]):
        if df_columns.loc[i]['Porc_nulos'] >= porc_nulos:
            tipos.append('Nula')
        elif df_columns.loc[i]['Porc_frec_max'] >= porc_lim_unitario:
            tipos.append('Unitaria')
        elif df_columns.loc[i]['Type'] != 'int64' and df_columns.loc[i]['Type'] != 'float64':
            if df_columns.loc[i]['Porc_unique'] < porc_unique_text:
                tipos.append('Discreta')
            else:
                tipos.append('Texto')
        elif df_columns.loc[i]['Porc_unique'] < porc_unique_num:
            tipos.append('Discreta')
        else:
            tipos.append('Continua')
    df_columns['Tipo'] = tipos
    return df_columns
