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
        cursor.execute("INSERT INTO usuarios (nombre, password, email, superUser) VALUES ('Usuario'+str(num_usuario), 'password'+str(num_usuario)+str(num_usuario+1)+str(num_usuario+2), 'usuario'+str(num_usuario)+'@gmail.com', 0)")
        cursor.execute("INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES ('Pelicula'+str(num_usuario), 'Acción', 120, 10)")
        # Comprueba que exista un usuario y una pelicula para poder insertar un registro en la tabla rentar
        cursor.execute("SELECT * FROM usuarios")
        usuario = cursor.fetchone()
        cursor.execute("SELECT * FROM peliculas")
        pelicula = cursor.fetchone()
        if usuario and pelicula:
            cursor.execute("INSERT INTO rentar (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus) VALUES (str(usuario), str(pelicula), '2023-18-02', 5, 0)")
        else:
            print("No se pudo insertar el registro en la tabla rentar porque no existen más registros en las tablas usuarios y peliculas")
        conn.commit()
    except Exception as e:
        print("No se pudo insertar el registro: ", e)
    finally:
        cursor.close()
        conn.close()