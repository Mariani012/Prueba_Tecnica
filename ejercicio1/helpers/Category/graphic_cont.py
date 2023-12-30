from bokeh.io import show
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from bokeh.io import output_notebook
from bokeh.palettes import PuBu
from bokeh.layouts import gridplot
from bokeh.models import CDSView, ColumnDataSource, IndexFilter
from ejercicio1.helpers.Category import category_classification
from ejercicio1.helpers.Read import read

df_dataset = read.cargar_archivo_csv()
df_columns = category_classification.variables_classifier(df_dataset)

# discrete_field vard[0]
vard = df_columns[df_columns['Tipo'] == 'Discreta']['Categoría'].to_list()
# continuous_field
varc = df_columns[df_columns['Tipo'] == 'Continua']['Categoría'].to_list()

"""Discrete Field Graphs"""


def graf_disc1(discrete_field):
    """ Bar graphic.

    Generates a bar graph of the discrete variables, in this case of the 'status' field.

    Args:
      discrete_field: List of fields containing discrete variables

    Returns:
         A Bar graphic with information from the 'status' column.
    """
    datos = df_dataset[discrete_field].value_counts().index.tolist()
    counts = df_dataset[discrete_field].value_counts()

    source = ColumnDataSource(data=dict(datos=datos, counts=counts))

    p = figure(x_range=datos, height=350, toolbar_location=None, title=str(discrete_field))
    p.vbar(x='datos', top='counts', width=0.8, source=source, legend_field="datos",
           line_color='white', fill_color=factor_cmap('datos', palette=PuBu[len(datos) - 1], factors=datos))

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.y_range.end = 15
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"

    output_notebook()
    return show(p)


"""###Continuous Field Graphs"""


def graf_cont1(continuous_field):
    """ Graphic to identify outliers.

    Generate a graph to identify the outliers of the continuous variables,
    in this case of the 'amount' field.

    Args:
      continuous_field: List of fields containing continuous variables.

    Returns:
         A Graphic with information from the 'amount' column.
    """
    tools = ["box_select", "hover", "reset"]
    p = figure(title=str(continuous_field), height=300, width=300, tools=tools)
    p.segment(0, df_dataset[continuous_field].value_counts(), df_dataset[continuous_field]
              .value_counts().index.tolist(),
              df_dataset[continuous_field].value_counts(), line_width=2, line_color="blue")
    p.circle(df_dataset[continuous_field].value_counts().index.tolist(), df_dataset[continuous_field].value_counts(),
             size=15, fill_color="skyblue", line_color="blue", line_width=3, )
    output_notebook()
    return show(gridplot([[p]]))


def graf_cont2(continuous_field):
    """ Graphic to identify outliers.

    Generate a graph to identify the outliers of the continuous variables,
    in this case of the 'amount' field.

    Args:
      continuous_field: List of fields containing continuous variables.

    Returns:
         A Graphic with information from the 'amount' column.
    """
    source = ColumnDataSource(data=dict(x=df_dataset[continuous_field].value_counts().index.tolist(),
                                        y=df_dataset[continuous_field].value_counts()))
    view = CDSView(source=source, filters=[IndexFilter([0, 1, 2])])

    tools = ["box_select", "hover", "reset"]
    p = figure(title=str(continuous_field), height=300, width=300, tools=tools)
    p.circle(x="x", y="y", size=10, hover_color="red", source=source)
    p.line(df_dataset[continuous_field].value_counts().index.tolist(), df_dataset[continuous_field].value_counts(),
           line_width=2, line_color="skyblue")

    p_filtered = figure(height=300, width=300, tools=tools)
    p_filtered.circle(x="x", y="y", size=10, hover_color="steelblue",
                      source=source, view=view)
    output_notebook()
    return show(gridplot([[p, p_filtered]]))
