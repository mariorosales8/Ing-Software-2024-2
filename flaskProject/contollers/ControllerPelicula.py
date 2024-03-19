from flask import Blueprint, request, render_template, flash, url_for
from random import randint
from alchemyClasses import db
from alchemyClasses.Pelicula import Pelicula

pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')

@pelicula_blueprint.route('/') #localhost:5000/pelicula/
def ver_peliculas():
    return render_template('movie.html')

#responde a localhost:5000/pelicula/id/1
@pelicula_blueprint.route('/id/<int:id_pelicula>/<string:nombre>') #<tipo:nombre_variable>
def ver_pelicula_id(id_pelicula, nombre):
    return f"Se hace el query con el id {id_pelicula} y el nombre {nombre}"


@pelicula_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_pelicula():
    if request.method == 'GET':
        return render_template('add_movie.html')
    else:
        try:
            #Obtengo la información del método post.
            nombre = request.form['nombre'].encode('utf-8')
            genero = request.form['genero'].encode('utf-8')
            duracion = request.form['duracion']
            inventario = request.form['inventario']
            #Creo mi pelicula.
            pelicula = Pelicula(nombre, genero, duracion, inventario)
            #Lo guardo en la DB
            db.session.add(pelicula)
            db.session.commit()

            # Redirijo a la vista principal.
            return render_template('movie.html')

        except Exception as e:
            db.session.rollback()
            flash('No se pudo agregar la película', 'error')
            return render_template('add_movie.html')