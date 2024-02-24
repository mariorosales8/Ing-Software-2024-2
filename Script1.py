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


insertar_registros()