# Base de Datos Comunal

Este proyecto tiene como objetivo principal la creación de una base de datos que recopile información detallada sobre las comunas de Chile. La base de datos está diseñada para almacenar información relacionada con aspectos como entretenimiento, trabajo, salud y educación en cada comuna. Además, se han desarrollado consultas predefinidas y se permite la ejecución de consultas personalizadas.

## Estructura de la Base de Datos

La base de datos se organiza en las siguientes tablas:

1. `Pais`: Almacena información sobre los países, como su identificador y nombre.

2. `Region`: Contiene información sobre las regiones de Chile, incluyendo su identificador, el identificador del país al que pertenecen y el nombre de la región.

3. `Comuna`: Almacena información sobre las comunas, como su identificador, el identificador de la región a la que pertenecen, el nombre de la comuna y su población.

4. `Entretencion`: Esta tabla registra los distintos tipos de entretenimiento disponibles en cada comuna. Incluye información como el identificador del entretenimiento, el identificador de la comuna, la categoría de entretenimiento, el nombre del entretenimiento y la ubicación del mismo.

5. `Educacion`: Contiene información sobre las instituciones educativas presentes en cada comuna. Incluye el identificador de la institución, el identificador de la comuna, el nombre de la institución, el nivel educativo y la afiliación de la institución.

6. `Panorama_Laboral`: Almacena información relacionada con el panorama laboral de cada comuna. Incluye el identificador del panorama laboral, el identificador de la comuna, la población en edad de trabajar, la cantidad de hombres y mujeres en edad de trabajar, y la cantidad de hombres y mujeres ocupados.

7. `Centros_de_salud`: Esta tabla registra los centros de salud disponibles en cada comuna. Incluye información como el identificador del centro de salud, el identificador de la comuna, el nombre del centro, el tipo de centro y la afiliación del centro.

8. `Indicadores`: Almacena indicadores específicos que permiten calificar y comparar el desarrollo y calidad de vida en cada comuna. Incluye el identificador de la comuna, los indicadores de entretenimiento, educación, panorama laboral, salud y el indicador total.

## Versión del Motor de Base de Datos

La base de datos ha sido implementada utilizando el motor de base de datos relacional MariaDB versión 11.1.0.

## Uso de la Base de Datos

Para utilizar esta base de datos, sigue los siguientes pasos:

1. Asegúrate de tener MariaDB versión 11.1.0 o superior instalado en tu sistema.

2. Descarga los archivos de la base de datos desde el repositorio [Nombre del repositorio].

3. Crea una nueva base de datos en MariaDB utilizando el archivo de creación de tablas y relaciones proporcionado.

4. Carga los datos en la base de datos ejecutando el script de carga de datos proporcionado.

5. Accede a la base de datos recién creada y ejecuta las consultas predefinidas para obtener información sobre las comunas, su entretenimiento, trabajo, salud y educación.

6. Si deseas realizar consultas personalizadas, utiliza la opción correspondiente en el menú y proporciona la consulta SQL deseada.

## Menú de Consultas

El programa proporciona un menú de opciones predefinidas que permiten ejecutar consultas específicas sobre la base de datos. Estas consultas incluyen:

1. Obtener la cantidad de centros de salud por comuna y ordenar de forma descendente.

2. Obtener la comuna con mayor población de cada región.

3. Cantidad de entretenimientos de cada categoría en una comuna según su identificador.

4. Comuna con mayor número de centros educativos por nivel educativo.

5. Número de comunas que tienen al menos un centro de entretenimiento, centro educativo y centro de salud.

6. Comuna con un panorama laboral donde la cantidad de mujeres ocupadas sea mayor a la cantidad de hombres ocupados.

7. Comunas en donde la cantidad de población es superior al promedio de la población de todas las comunas.

8. Comuna con mayor cantidad de centros de salud según el tipo de centro de salud.

9. Porcentaje de ocupación laboral de hombres y mujeres en todas las comunas.

10. Cantidad de centros educativos por comuna desglosados por nivel educativo.

11. Comuna con mayor porcentaje de ocupación laboral en mujeres respecto a la población en edad de trabajar.

12. Comunas que tienen una población mayor al promedio de su respectiva región.

13. Porcentaje de ocupación laboral de mujeres por región.

14. Consulta personalizada: Permite al usuario ingresar una consulta SQL personalizada.

## Contribuyentes

- Rodrigo Vargas
- Vicente Muñoz
- Edgardo Dorner