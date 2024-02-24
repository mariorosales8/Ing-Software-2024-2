from flask import Flask
from alchemyClasses import db
from alchemyClasses.Usuario import Usuario
from alchemyClasses.Pelicula import Pelicula
from alchemyClasses.Rentar import Rentar

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_software'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)


def ver_registros():
    print("Seleccione la tabla:")
    print("1. Usuarios")
    print("2. Peliculas")
    print("3. Rentas")
    opcion = input("Opción: ")

    if opcion == '1':
        print()
        for usuario in Usuario.query.all():
            print(usuario)
    elif opcion == '2':
        print()
        for pelicula in Pelicula.query.all():
            print(pelicula)
    elif opcion == '3':
        print()
        for renta in Rentar.query.all():
            print(renta)
    else:
        print("Opción inválida")

def filtrar_por_id():
    print("Seleccione la tabla:")
    print("1. Usuarios")
    print("2. Peliculas")
    print("3. Rentas")
    opcion = input("Opción: ")
    id = input("Ingrese el ID a buscar: ")

    if opcion == '1':
        usuarios = Usuario.query.filter_by(idUsuario=id).all()
        print()
        if len(usuarios) > 0:
            for usuario in usuarios:
                print(usuario)
        else:
            print("No se encontró.")
    if opcion == '2':
        peliculas = Pelicula.query.filter_by(idPelicula=id).all()
        print()
        if len(peliculas) > 0:
            for pelicula in peliculas:
                print(pelicula)
        else:
            print("No se encontró.")
    if opcion == '3':
        rentas = Rentar.query.filter_by(idRentar=id).all()
        print()
        if len(rentas) > 0:
            for renta in rentas:
                print(renta)
        else:
            print("No se encontró.")

def actualizar_registro():
    print("Seleccione la tabla:")
    print("1. Usuarios")
    print("2. Peliculas")
    print("3. Rentas")
    opcion = input("Opción: ")
    id = input("Ingrese el ID del registro a actualizar: ")

    if opcion == '1':
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        usuario = Usuario.query.filter_by(idUsuario=id).first()
        if usuario:
            usuario.nombre = nuevo_nombre
            db.session.commit()
            print()
            print("Nombre de usuario actualizado correctamente.")
        else:
            print()
            print("Usuario no encontrado.")
    if opcion == '2':
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        pelicula = Pelicula.query.filter_by(idPelicula=id).first()
        if pelicula:
            pelicula.nombre = nuevo_nombre
            db.session.commit()
            print()
            print("Nombre de la película actualizado correctamente.")
        else:
            print()
            print("Película no encontrada.")
    if opcion == '3':
        nueva_fecha = input("Ingrese la nueva fecha (YYYY-MM-DD): ")
        renta = Rentar.query.filter_by(idRentar=id).first()
        if renta:
            renta.fecha_renta = nueva_fecha
            db.session.commit()
            print()
            print("Fecha de renta actualizada correctamente.")
        else:
            print()
            print("Renta no encontrada.")

def eliminar_registro():
    print("Seleccione la tabla:")
    print("1. Usuarios")
    print("2. Peliculas")
    print("3. Rentas")
    opcion = input("Opción: ")
    id = input("Ingrese el ID del registro a eliminar (o -1 para eliminar todos los registros): ")

    if opcion == '1':
        if id == '-1':
            usuarios = Usuario.query.all()
        else:
            usuarios = Usuario.query.filter_by(idUsuario=id).all()
        for usuario in usuarios:
            db.session.delete(usuario)
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print("Error al eliminar los registros")
    if opcion == '2':
        if id == '-1':
            peliculas = Pelicula.query.all()
        else:
            peliculas = Pelicula.query.filter_by(idPelicula=id).all()
        for pelicula in peliculas:
            db.session.delete(pelicula)
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print("Error al eliminar los registros")
    if opcion == '3':
        if id == '-1':
            rentas = Rentar.query.all()
        else:
            rentas = Rentar.query.filter_by(idRentar=id).all()
        for renta in rentas:
            db.session.delete(renta)
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print("Error al eliminar los registros")




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        while True:
            print("\nMenú Principal")
            print("1. Ver los registros de una tabla.")
            print("2. Filtrar los registros de una tabla por id.")
            print("3. Actualizar una columna de un registro.")
            print("4. Eliminar un registro.")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                ver_registros()
            elif opcion == '2':
                filtrar_por_id()
            elif opcion == '3':
                actualizar_registro()
            elif opcion == '4':
                eliminar_registro()
            elif opcion == '5':
                print("Saliendo del programa.")
                break
            else:
                print("Opción inválida.")


