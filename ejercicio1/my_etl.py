from ejercicio1.exercise import processed_exercise

if __name__ == "__main__":
    """ Query in the dataset about sales.
    
    Returns:
         Ten Queries in the dataset about daily sales by companies and their status
    """
    sales_day_company, sales_day_comp_status, sales_amount, amount_functions, sales_different_voided, sales_canceled, amount_sales_can_pasajefy, amount_sales_can_muebles, amount_paid_sales, amount_pending_sales = processed_exercise.sales_analysis()

    print(sales_day_company)
