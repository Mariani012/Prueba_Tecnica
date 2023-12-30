def trat_outliers(df_dataset, field):

    """ Treatment of outliers.

   Treatment of outliers for continuous variables.

    Args:
      df_dataset: Dataframe that contains information about payments from different companies.
      field:  List of fields containing continuous variables.

    Returns:
         A dataframe with the reduction of outliers through the quantile method.
    """
    seventy_fifth = df_dataset[field].quantile(0.75)
    twenty_fifth = df_dataset[field].quantile(0.25)
    iqr = seventy_fifth - twenty_fifth
    lim_max = seventy_fifth + (1.5 * iqr)
    lim_min = twenty_fifth + (1.5 * iqr)

    for i in range(len(field)):
        df_dataset = df_dataset[(df_dataset[field[i]] > lim_min.iloc[i]) &
                                (df_dataset[field[i]] < lim_max.iloc[i])]
    return df_dataset
