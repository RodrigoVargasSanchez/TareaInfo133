import mysql.connector

def ejecutar_consulta(sql):
    # Establecer la conexión con la base de datos
    conexion = mysql.connector.connect(
        host="localhost",
        user="edorner",
        password="edgardo1",
        database="Información_territorial_basada_en_las_comunas_de_Chile"
    )

    # Crear un cursor para ejecutar consultas
    cursor = conexion.cursor()

    try:
        # Ejecutar la consulta SQL
        cursor.execute(sql)

        # Obtener los resultados de la consulta
        resultados = cursor.fetchall()

        # Imprimir los resultados
        for fila in resultados:
            print(fila)

    except mysql.connector.Error as error:
        print("Error al ejecutar la consulta: ", error)

    finally:
        # Cerrar el cursor y la conexión a la base de datos
        cursor.close()
        conexion.close()

# Menú de opciones
while True:
    print("Seleccione una opción:")
    print("1. Obtener la cantidad de centros de salud por comuna y ordenar de forma descendente")
    print("2. Obtener la comuna con mayor población de cada región")
    print("3. Cantidad de entretenciones de cada categoría de una comuna según su id")
    print("4. Comuna con mayor número de centros educativos por nivel educativo")
    print("5. Número de comunas que tiene al menos un centro de entretención, centro educativo y centro de salud")
    print("6. Comuna con un panorama laboral donde la cantidad de mujeres ocupadas sea mayor a la cantidad de hombres ocupados")
    print("7. Comunas en donde la cantidad de población es superior al promedio de la población de todas las comunas")
    print("8. Comuna con mayor cantidad de centros de salud según el tipo de centro de salud")
    print("9. Porcentaje de ocupación laboral de hombres y mujeres en todas las comunas")
    print("10. Cantidad de centros educativos por comuna desglosados por nivel educativo")
    print("11. Comuna con mayor porcentaje de ocupación laboral en mujeres respecto a la población en edad de trabajar")
    print("12. Comunas que tienen una población mayor al promedio de su respectiva región")
    print("13. Porcentaje de ocupación laboral de mujeres por región")
    print("14. Consulta personalizada")
    print("0. Salir")

    opcion = int(input("Opción seleccionada: "))

    if opcion == 0:
        break

    elif opcion == 1:
        sql = "SELECT c.nombre_comuna, COUNT(cs.id_centro) AS cantidad_centros_salud\n" \
              "FROM Comuna c\n" \
              "LEFT JOIN Centros_de_salud cs ON c.id_comuna = cs.id_comuna\n" \
              "GROUP BY c.id_comuna, c.nombre_comuna\n" \
              "ORDER BY cantidad_centros_salud DESC;"
        ejecutar_consulta(sql)

    elif opcion == 2:
        sql = "SELECT r.nombre_region, c.nombre_comuna, c.poblacion\n" \
              "FROM Region r\n" \
              "JOIN (\n" \
              "    SELECT id_region, nombre_comuna, poblacion, ROW_NUMBER() OVER (PARTITION BY id_region ORDER BY poblacion DESC) AS rn\n" \
              "    FROM Comuna\n" \
              ") c ON r.id_region = c.id_region AND c.rn = 1;"
        ejecutar_consulta(sql)

    elif opcion == 3:
        id_comuna = int(input("Ingrese el ID de la comuna: "))
        sql = "SELECT categoria_entretencion, COUNT(*) AS cantidad_entretenciones\n" \
              "FROM Entretencion\n" \
              f"WHERE id_comuna = {id_comuna}\n" \
              "GROUP BY categoria_entretencion;"
        ejecutar_consulta(sql)

    elif opcion == 4:
        sql = "SELECT e.nivel, c.nombre_comuna, COUNT(e.id_institucion) AS cantidad_instituciones\n" \
              "FROM Educacion e\n" \
              "JOIN Comuna c ON e.id_comuna = c.id_comuna\n" \
              "GROUP BY e.nivel, c.nombre_comuna\n" \
              "HAVING COUNT(e.id_institucion) = (\n" \
              "    SELECT MAX(cnt)\n" \
              "    FROM (\n" \
              "        SELECT COUNT(id_institucion) AS cnt\n" \
              "        FROM Educacion\n" \
              "        GROUP BY id_comuna, nivel\n" \
              "    ) AS subquery\n" \
              ");"
        ejecutar_consulta(sql)

    elif opcion == 5:
        sql = "SELECT COUNT(*) AS cantidad_comunas\n" \
              "FROM (\n" \
              "    SELECT c.id_comuna\n" \
              "    FROM Comuna c\n" \
              "    JOIN Entretencion e ON c.id_comuna = e.id_comuna\n" \
              "    JOIN Educacion ed ON c.id_comuna = ed.id_comuna\n" \
              "    JOIN Centros_de_salud cs ON c.id_comuna = cs.id_comuna\n" \
              "    GROUP BY c.id_comuna\n" \
              "    HAVING COUNT(DISTINCT e.id_entretencion) > 0 AND COUNT(DISTINCT ed.id_institucion) > 0 AND COUNT(DISTINCT cs.id_centro) > 0\n" \
              ") AS subquery;"
        ejecutar_consulta(sql)

    elif opcion == 6:
        sql = "SELECT c.nombre_comuna\n" \
              "FROM Comuna c\n" \
              "JOIN Panorama_Laboral pl ON c.id_comuna = pl.id_comuna\n" \
              "WHERE pl.muj_ocupadas > pl.hom_ocupados;"
        ejecutar_consulta(sql)

    elif opcion == 7:
        sql = "SELECT c.nombre_comuna, c.poblacion\n" \
              "FROM Comuna c\n" \
              "WHERE c.poblacion > (SELECT AVG(poblacion) FROM Comuna);"

        ejecutar_consulta(sql)

    elif opcion == 8:
        sql = "SELECT cs.tipo_centro, c.nombre_comuna, COUNT(cs.id_centro) AS cantidad_centros_salud\n" \
              "FROM Comuna c\n" \
              "JOIN Centros_de_salud cs ON c.id_comuna = cs.id_comuna\n" \
              "GROUP BY cs.tipo_centro, c.nombre_comuna\n" \
              "HAVING COUNT(cs.id_centro) = (\n" \
              "    SELECT MAX(cnt)\n" \
              "    FROM (\n" \
              "        SELECT COUNT(id_centro) AS cnt\n" \
              "        FROM Centros_de_salud\n" \
              "        GROUP BY id_comuna, tipo_centro\n" \
              "    ) AS subquery\n" \
              ");"
        ejecutar_consulta(sql)

    elif opcion == 9:
        sql = "SELECT c.nombre_comuna, pl.hom_ocupados * 100 / pl.pob_edad_trabajar AS porcentaje_hombres, pl.muj_ocupadas * 100 / pl.pob_edad_trabajar AS porcentaje_mujeres\n" \
              "FROM Comuna c\n" \
              "JOIN Panorama_Laboral pl ON c.id_comuna = pl.id_comuna\n" \
              "ORDER BY porcentaje_hombres DESC;"
        ejecutar_consulta(sql)

    elif opcion == 10:
        sql = "SELECT c.nombre_comuna, e.nivel, COUNT(e.id_institucion) AS cantidad_instituciones\n" \
              "FROM Comuna c\n" \
              "JOIN Educacion e ON c.id_comuna = e.id_comuna\n" \
              "GROUP BY c.nombre_comuna, e.nivel;"
        ejecutar_consulta(sql)

    elif opcion == 11:
        sql = "SELECT c.nombre_comuna, (pl.muj_ocupadas * 100 / pl.pob_edad_trabajar) AS porcentaje_mujeres_ocupadas\n" \
              "FROM Comuna c\n" \
              "JOIN Panorama_Laboral pl ON c.id_comuna = pl.id_comuna\n" \
              "ORDER BY porcentaje_mujeres_ocupadas DESC\n" \
              "LIMIT 1;"
        ejecutar_consulta(sql)

    elif opcion == 12:
        sql = "SELECT c.nombre_comuna, c.poblacion, r.nombre_region\n" \
              "FROM Comuna c\n" \
              "JOIN Region r ON c.id_region = r.id_region\n" \
              "WHERE c.poblacion > (\n" \
              "    SELECT AVG(poblacion)\n" \
              "    FROM Comuna\n" \
              "    WHERE id_region = c.id_region\n" \
              ")"
        ejecutar_consulta(sql)

    elif opcion == 13:
        sql = "SELECT r.nombre_region, SUM(pl.muj_ocupadas) * 100 / SUM(pl.pob_edad_trabajar) AS porcentaje_mujeres_ocupadas\n" \
              "FROM Region r\n" \
              "JOIN Comuna c ON r.id_region = c.id_region\n" \
              "JOIN Panorama_Laboral pl ON c.id_comuna = pl.id_comuna\n" \
              "GROUP BY r.nombre_region\n" \
              "ORDER BY porcentaje_mujeres_ocupadas DESC;"
        ejecutar_consulta(sql)
    
    elif opcion == 14:
        consulta_personalizada = input("Ingrese su consulta SQL personalizada: ")
        ejecutar_consulta(consulta_personalizada)

    print()
