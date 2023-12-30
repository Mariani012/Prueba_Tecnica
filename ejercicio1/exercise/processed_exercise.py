import numpy as np
import pandas as pd

from ejercicio1.processed import processed


def sales_analysis():
    """ Query in the dataset about sales.

    Queries in the dataset about daily sales by companies and their status.

    Returns:
         Ten Queries in the dataset about daily sales by companies and their status
    """
    dataset = processed.dataset_processed()

    # Daily Sales by company
    sales_day_company_e = dataset.groupby(['created_at', 'name']).agg({'name': ['count']})

    # Daily Sales by company and status
    sales_day_comp_status_e = dataset.groupby(['created_at', 'name', 'status']).agg({'name': ['count']})

    # Daily sales amount by company
    sales_amount_e = dataset.groupby(['created_at', 'name']).agg({'amount': ['sum']})

    # Maximum, minimum, average daily sales by company
    amount_functions_e = dataset.groupby(['created_at', 'name']).agg({'amount': ['max', 'min', np.mean]})

    # Daily sales that do not contain voided sales
    sales_different_voided_e = (dataset[dataset['status'] != 'voided'].groupby(['created_at', 'name'])
                                .agg({'name': ['count']}))

    # Amount of daily sales canceled
    sales_canceled_e = dataset[dataset['status'] == 'voided'].groupby(['created_at', 'name']).agg({'amount': ['sum']})

    # Amount of canceled sales of the company 'MiPasajefy'
    amount_sales_can_pasajefy_e = (dataset[(dataset['status'] == 'voided') & (dataset['name'] == 'MiPasajefy')]
                                   .groupby(['created_at', 'name']).agg({'amount': ['sum']}))

    # Amount of canceled sales of the company 'Muebles chidos'
    amount_sales_can_muebles_e = (dataset[(dataset['status'] == 'voided') & (dataset['name'] != 'MiPasajefy')]
                                  .groupby(['created_at', 'name']).agg({'amount': ['sum']}))

    #  Amount of paid sales of the company 'MiPasajefy'
    amount_paid_sales_e = (dataset[(dataset['status'] == 'paid') & (dataset['name'] == 'MiPasajefy')]
                           .groupby(['created_at', 'name']).agg({'amount': ['sum']}))

    # Amount of sales pending payment of the company 'MiPasajefy'
    amount_pending_sales_e = (dataset[(dataset['status'] == 'pending_payment') & (dataset['name'] == 'Muebles chidos')]
                              .groupby(['created_at', 'name']).agg({'amount': ['sum']}))

    return (sales_day_company_e, sales_day_comp_status_e, sales_amount_e, amount_functions_e,
            sales_different_voided_e, sales_canceled_e, amount_sales_can_pasajefy_e,
            amount_sales_can_muebles_e, amount_paid_sales_e, amount_pending_sales_e)


if __name__ == "__main__":
    sales_day_company, sales_day_comp_status, sales_amount, amount_functions, sales_different_voided, sales_canceled, amount_sales_can_pasajefy, amount_sales_can_muebles, amount_paid_sales, amount_pending_sales = sales_analysis()

    print(amount_functions)
