from flask import Blueprint, request, render_template, flash, url_for, redirect
from random import randint
from alchemyClasses import db
from alchemyClasses.Pelicula import Pelicula

pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')

@pelicula_blueprint.route('/') #localhost:5000/pelicula/
def index_peliculas():
    return render_template('movie.html')

@pelicula_blueprint.route('/consultar') #localhost:5000/pelicula/consultar
def ver_peliculas():
    # Recupera todas las películas de la base de datos
    peliculas = Pelicula.query.all()
    return render_template('read_movies.html', peliculas=peliculas)

@pelicula_blueprint.route('/eliminar', methods=['GET', 'POST'])#responde a localhost:5000/pelicula/eliminar
def borrar_pelicula():
    if request.method == 'GET':
        return render_template('delete_movie.html')
    else:
        try:
            #Busco la película por su id
            ide_pelicula = request.form['id']
            pelicula = Pelicula.query.get(ide_pelicula)
            #Lo elimino de la base de datos
            db.session.delete(pelicula)
            db.session.commit()
            # Redirijo a la vista principal.
            return render_template('movie.html')
        except Exception as e:
            db.session.rollback()
            flash('No se pudo eliminar la película', 'error')
            return render_template('delete_movie.html')

@pelicula_blueprint.route('/actualizar', methods=['GET', 'POST']) #localhost:5000/pelicula/actualizar
def actualizar_pelicula():
    if request.method == 'POST':
        try:
            pelicula_id = request.form['id']
            # Redirige a la vista de actualización con el ID de la pelicula proporcionado
            return redirect(url_for('pelicula.actualizar_datos', pelicula_id=pelicula_id))
        except Exception as e:
            db.session.rollback()
            flash('No se pudo actualizar la película', 'error')
            return render_template('update_movie.html')
    return render_template('update_movie.html')

@pelicula_blueprint.route('/actualizar/<int:pelicula_id>', methods=['GET', 'POST'])
def actualizar_datos(pelicula_id):
    pelicula = Pelicula.query.get(pelicula_id)
    if pelicula is None:
        flash('No se encontró la película', 'error')
        return redirect(url_for('pelicula.actualizar_pelicula'))
    if request.method == 'POST':
        try:
            # Actualiza los datos de la película
            pelicula.nombre = request.form['name'].encode('utf-8')
            pelicula.genero = request.form['genero'].encode('utf-8')
            pelicula.duracion = request.form['duracion']
            pelicula.inventario = request.form['inventario']
            db.session.commit()
            return render_template('movie.html')
        except Exception as e:
            db.session.rollback()
            flash('No se pudo actualizar la película', 'error')
            return render_template('updating_movie.html', pelicula=pelicula)
    return render_template('updating_movie.html', pelicula=pelicula)

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