# Prueba_Tecnica

Consideraciones:
* En el módulo  Read para la ruta al archivo CSV (ajusta la ruta según tu estructura de carpetas)
* Para la parte de gráficos instalar bokeh
* las variables varc y vard se generan de la siguiente manera, en caso de requerirlo
* Se adjuntó el archivo .ipynb ya que ahí esta el análisis completo y debido a la versión de python de mi
  computadora no pude adjuntar la función para el conteo de outliers con la paquetería pyod. 

EJERCICIO 1
1. Para los id nulos, ¿qué susugieres hacer con ellos?
    Debido a que los valores nulos eran muy pocos se ofrece un tratamiendo de sustitución con a "moda"

2. Considerando las columnas name y company_id ¿Qué inconsistencias notas y cómo mitigas? 
    En la columna de 'name' habían nombres mal escritos, que si bien se podría entender que fue por una mala escritura,
    se soluciono cuando se retiraron los valores atípicos que existían, si no se hubieran retirado se podría sustiur 
    los nombres por una categoría que tenga un nombre generico para todos ellos que estan mal escritos. 
    Para el caso de 'company_id' se entiente que esta tokenizado y por eso no se muestra el nombre, 
    debido a eso son valores únicos, como parte de la mejora pondría otra columna que se relacione con esta para más
    para saber que son del mismo id.

3. Para el resto de los campos, ¿Encuentras valores atípicos y de ser así cómo procedes?
    Sí se encontraron valores atícos, unos que realmente modificaban mucho el análisis de la data, se hizo una función
    para saber el número de outliers que existían con una paquetería llamada pyod, del resultado se hicieron varias pruebas,
    y al final se ejecuto un tratamiento que consiste que quedarán los valores dentro de los quantiles 0.75 y 0.25, haciendo
    que la data se redujera, aquí se hizo el cuestionamiento de qué importaba más si el número de registros y
    permanecer con los outliers sustiyendo con otro valor o mejor retirarlos, y se decidió retirarlos y pro eso se aplicó el
    tratamiento anterior

4. Qué mejoras propondrías a tu proceso ETL para siguientes versiones?
    Considería el número de registros, más columnas, tal vez como el producto por el cuál fue la transacción para hacer un análisis
    más completo, agregar la parde de los id como se mencionó en el número 2.

