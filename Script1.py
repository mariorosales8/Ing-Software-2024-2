import datetime

import pymysql

num_usuario = 0

config = {
    'host': 'localhost',
    'user': 'lab',
    'password': 'Developer123!',
    'database': 'lab_ing_software',
}

# Ejercicio 2.1.1
def insertar_registros():
    try:
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        # Inserta usuario
        sql_usuarios = """
                    INSERT INTO usuarios (nombre, apPat, apMat, password, email, superUser)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """
        cursor.execute(sql_usuarios, ('Juan',
                                      'Pérez',
                                      'Gonzáles',
                                      'Developer123!',
                                      'juanpgonz@gmail.com',
                                      False))
        id_usuario = cursor.lastrowid

        # Inserta película
        sql_peliculas = """
                    INSERT INTO peliculas (nombre, genero, duracion, inventario)
                    VALUES (%s, %s, %s, %s)
                    """
        cursor.execute(sql_peliculas, ('Terminator',
                                           'Ciencia ficción',
                                           '110',
                                           1))
        id_pelicula = cursor.lastrowid

        # Ingresa rente
        sql_rentar = """
                    INSERT INTO rentar (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus)
                    VALUES (%s, %s, %s, %s, %s)
                    """
        cursor.execute(sql_rentar, (id_usuario, id_pelicula,
                                    datetime.datetime.now(), 5, 0))

        conn.commit()
    except Exception as e:
        print("No se pudo insertar el registro. Error: ", e)
    finally:
        cursor.close()
        conn.close()


# Ejercicio 2.1.2
def filtra_por_apellido(cadena_final):
    try:
        conn = pymysql.connect(**config)
        cursor = conn.cursor()

        query = """
                    SELECT *
                    FROM usuarios
                    WHERE apPat LIKE %s OR apMat LIKE %s
                """
        filtro = '%' + cadena_final
        cursor.execute(query, (filtro, filtro))
        conn.commit()
    except Exception as e:
        print("Error: ", e)
    finally:
        cursor.close()
        conn.close()
        return cursor.fetchall()

# Ejercicio 2.1.3
def cambia_genero(nombre, genero):
    try:
        conn = pymysql.connect(**config)
        cursor = conn.cursor()

        query = "SELECT idPelicula FROM peliculas WHERE nombre = %s"
        cursor.execute(query, nombre)
        pelicula = cursor.fetchone()

        if pelicula:
            sql_actualiza = "UPDATE peliculas SET genero = %s WHERE nombre = %s"
            cursor.execute(sql_actualiza, (genero, nombre))

        conn.commit()
    except Exception as e:
        print("Error: ", e)
    finally:
        cursor.close()
        conn.close()

# Ejercicio 2.1.4
def elimina_rentas():
    try:
        conn = pymysql.connect(**config)
        cursor = conn.cursor()

        fecha_limite = datetime.datetime.now() - datetime.timedelta(days=3)
        fecha_limite_str = fecha_limite.strftime('%Y-%m-%d %H:%M:%S')

        sql_elimina = "DELETE FROM rentar WHERE fecha_renta < %s"
        cursor.execute(sql_elimina, fecha_limite_str)

        conn.commit()
    except Exception as e:
        print("Error: ", e)
    finally:
        cursor.close()
        conn.close()
