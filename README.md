# Base de Datos Comunal

Este proyecto tiene como objetivo crear una base de datos que almacene información comunal relacionada con aspectos como entretenimiento, trabajo, salud y educación. A continuación se presenta una explicación de cada componente de la base de datos:

## Estructura de la Base de Datos

La base de datos se organiza en las siguientes tablas:

1. `Comunas`: Esta tabla almacena información sobre cada comuna, como su nombre, población, país y región.

2. `Entretencion`: Aquí se registran los distintos tipos de entretenimiento disponibles en cada comuna, como cines, casinos y estadios.

3. `Trabajo`: En esta tabla se recopila información sobre el empleo en cada comuna, incluyendo tanto hombres como mujeres empleados y desempleados.

4. `Salud`: Aquí se almacenan datos relacionados con los servicios de salud disponibles en cada comuna, como hospitales, clínicas, centros de atención primaria, especialidades médicas y relacionados.

5. `Educacion`: Esta tabla contiene información sobre las instituciones educativas presentes en cada comuna, tanto de educación superior como básica y media, ya sea establecimientos privados o públicos.

6. `Indicadores`: La tabla "Indicadores" está relacionada de forma 1:1 con la tabla "Comunas" y almacena indicadores específicos para cada comuna, como la cantidad de centros de entretenimiento, centros educativos, proporción laboral, cantidad de centros de salud y un indicador total que representa el promedio de todos los indicadores anteriores.

## Versión del Motor de Base de Datos

La base de datos ha sido implementada utilizando el motor de base de datos relacional MariaDB versión 11.1.0.

## Uso de la Base de Datos

Para utilizar esta base de datos, sigue los siguientes pasos:

1. Asegúrate de tener MariaDB versión 11.1.0 o superior instalado en tu sistema.

2. Descarga los archivos de la base de datos desde el repositorio (https://github.com/RodrigoVargasSanchez/TareaInfo133.git).

3. Crea una nueva base de datos en MariaDB y carga los archivos contenidos en la carpeta datos.

4. Accede a la base de datos recién creada y comienza a realizar consultas para obtener información sobre las comunas, su entretenimiento, trabajo, salud y educación.

## Indicadores

Dentro de la base de datos, se encuentra la tabla "Indicadores" que está relacionada de forma 1:1 con la tabla "Comuna". Esta tabla almacena indicadores específicos para cada comuna, los cuales se clasifican de la siguiente manera:

- **ind_entretencion**: Cantidad de centros de entretenimiento disponibles en la comuna.
  - Rango de valores:
    - Deficiente: [0, 0]
    - Aceptable: [1, 2]
    - Excelente: [3, ...]

- **ind_educacion**: Cantidad de centros educativos presentes en la comuna.
  - Rango de valores:
    - Deficiente: [1, 59]
    - Aceptable: [60, 99]
    - Excelente: [100, ...]

- **ind_laboral**: Proporción entre personas con trabajo y personas en edad de trabajar en la comuna.
  - Rango de valores:
    - Deficiente: [0, 0.5[
    - Aceptable: [0.5, 0.7[
    - Excelente: [0.7, 1]

- **ind_salud**: Cantidad de centros de salud disponibles en la comuna.
  - Rango de valores:
    - Deficiente: [1, 10[
    - Aceptable: [10, 30]
    - Excelente: [30, ...]

- **ind_total**: Promedio de todos los indicadores anteriores.

Cada indicador se clasifica en tres categorías: Deficiente, Aceptable y Excelente, y se le asigna un valor numérico según el siguiente sistema de puntajes:

- Deficiente: 0 puntos
- Aceptable: 1 punto
- Excelente: 2 puntos

El indicador total (ind_total) se calcula sumando los puntos obtenidos en cada indicador específico, y se le asigna una calificación de acuerdo al siguiente sistema de puntajes:

- Deficiente: [0, 1] puntos
- Aceptable: [2, 4] puntos
- Excelente: [5, 8] puntos

Este indicador total permite tener una medida general del desarrollo y calidad de vida en cada comuna, considerando los diferentes aspectos evaluados.

Por ejemplo, si tomamos la comuna de Santiago y se obtienen los siguientes valores:

- Cantidad de centros de entretenimiento: 7 (Excelente)
- Cantidad de centros educativos: 249 (Excelente)
- Proporción laboral: 0.7232 (Excelente)
- Cantidad de centros de salud: 64 (Excelente)

En este caso, el indicador total (ind_total) de la comuna de Santiago sería "Excelente", con un puntaje de 8 puntos.



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
