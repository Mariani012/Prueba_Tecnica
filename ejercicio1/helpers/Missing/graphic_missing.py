import pandas as pd
from bokeh.io import show
from bokeh.plotting import figure
from bokeh.io import output_notebook
from bokeh.transform import cumsum
from bokeh.palettes import PuBu
from math import pi
from ejercicio1.helpers.Category import category_classification
from ejercicio1.helpers.Read import read

df_dataset = read.cargar_archivo_csv()
df_columns = category_classification.variables_classifier(df_dataset)

# discrete_field vard
vard = df_columns[df_columns['Tipo'] == 'Discreta']['Categoría'].to_list()
# continuous_field
varc = df_columns[df_columns['Tipo'] == 'Continua']['Categoría'].to_list()

"""Graphics Function """


def valores_nulos(field):
    """ Graphic containing null value information.

    Generate a graph to identify the null values of the continuous or discrete variables.

    Args:
      field: List of fields containing continuous or discrete variables.

    Returns:
         A graph with information on the percentage of nulls for each field.
    """
    z = {'Nulos': df_dataset[field].isnull().sum(), 'No nulos': df_dataset[field].notnull().sum()}
    x = z
    data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'country'})
    data['angle'] = data['value'] / data['value'].sum() * 2 * pi
    if len(x) < 3:
        data['color'] = ['#084594', '#2171b5']
    else:
        data['color'] = PuBu[len(x)]
    p = figure(height=350, title=str(field), toolbar_location=None,
               tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='country', source=data)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None
    output_notebook()
    return show(p)


"""### Discrete Field Graphs"""

for c in vard:
    valores_nulos(c)

"""### Continuous Field Graphs"""

for c in varc:
    valores_nulos(c)
