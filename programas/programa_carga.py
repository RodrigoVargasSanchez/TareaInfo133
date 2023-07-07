import csv
import pymysql


conexion = pymysql.connect(host="localhost", user="edorner", password="edgardo1", database="Información_territorial_basada_en_las_comunas_de_Chile")

try:
    with conexion.cursor() as cursor:
        
        with open("../datos/Paises_Final.csv", "r") as archivo_csv:
            csv_data = csv.reader(archivo_csv, delimiter=";")
            next(csv_data)  
            for row in csv_data:
                cursor.execute("INSERT INTO Pais (id_pais, nombre_pais) VALUES (%s, %s)", row)
        
        
        with open("../datos/Regiones_Final.csv", "r") as archivo_csv:
            csv_data = csv.reader(archivo_csv, delimiter=",")
            next(csv_data)
            for row in csv_data:
                cursor.execute("INSERT INTO Region (id_region, id_pais, nombre_region) VALUES (%s, %s, %s)", row)
        
        
        with open("../datos/Comunas_Final.csv", "r") as archivo_csv:
            csv_data = csv.reader(archivo_csv, delimiter=",")
            next(csv_data)
            for row in csv_data:
                cursor.execute("INSERT INTO Comuna (id_comuna, id_region, nombre_comuna, poblacion) VALUES (%s, %s, %s, %s)", row)
        
        
        with open("../datos/Entretencion.csv", "r") as archivo_csv:
            csv_data = csv.reader(archivo_csv, delimiter=",")
            next(csv_data)
            for row in csv_data:
                cursor.execute("INSERT INTO Entretencion (id_entretencion, id_comuna, categoria_entretencion, nombre_entretencion, ubicacion_entretencion) VALUES (%s, %s, %s, %s, %s)", row)
        
        
        with open("../datos/Educacion.csv", "r") as archivo_csv:
            csv_data = csv.reader(archivo_csv, delimiter=",")
            next(csv_data)
            for row in csv_data:
                cursor.execute("INSERT INTO Educacion (id_institucion, id_comuna, nombre_institucion, nivel, afiliacion_institucion) VALUES (%s, %s, %s, %s, %s)", row)
        
        
        with open("../datos/Trabajo.csv", "r") as archivo_csv:
            csv_data = csv.reader(archivo_csv, delimiter=",")
            next(csv_data)
            for row in csv_data:
                cursor.execute("INSERT INTO Panorama_Laboral (id_panorama, id_comuna, pob_edad_trabajar, hom_edad_trabajar, muj_edad_trabajar, hom_ocupados, muj_ocupadas) VALUES (%s, %s, %s, %s, %s, %s, %s)", row)
        
        
        with open("../datos/Centros_de_Salud.csv", "r") as archivo_csv:
            csv_data = csv.reader(archivo_csv, delimiter=",")
            next(csv_data)
            for row in csv_data:
                cursor.execute("INSERT INTO Centros_de_salud (id_centro, id_comuna, nombre_centro, tipo_centro, afiliacion_centro) VALUES (%s, %s, %s, %s, %s)", row)

        with open("../datos/Indicadores.csv", "r") as archivo_csv:
            csv_data = csv.reader(archivo_csv, delimiter=",")
            next(csv_data)  
            for row in csv_data:
                cursor.execute("INSERT INTO Indicadores (id_comuna, ind_entretencion, ind_educacion, ind_laboral, ind_salud, ind_total) VALUES (%s, %s, %s, %s, %s, %s)", row)

    conexion.commit()
    print("Datos cargados correctamente.")

except Exception as e:
    
    conexion.rollback()
    print("Error -->", str(e))

finally:
    
    conexion.close()
