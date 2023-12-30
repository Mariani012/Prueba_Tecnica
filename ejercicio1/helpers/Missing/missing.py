def trat_null_disc(df_dataset, discrete_field, tratamiento_disc):
    """ Null value treatment.

    Treatment of null values for discrete variables.

    Args:
      df_dataset: Dataframe that contains information about payments from different companies .
      discrete_field: List of fields containing discrete variables
      tratamiento_disc: Method with which we are going to replace null values

    Returns:
         A dataframe with the null values replaced by the mode.
         example:
         'Nan' = 	"pending_payment"
    """
    if tratamiento_disc == 'moda':
        "Completando valores faltantes con la moda datos categóricos"
        for c in discrete_field:
            moda = df_dataset[c].mode()[0]
            df_dataset[c] = df_dataset[c].fillna(moda)
    return df_dataset
