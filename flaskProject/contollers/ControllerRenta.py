from flask import Blueprint, request, render_template, flash, url_for, redirect
from random import randint
from alchemyClasses import db
from alchemyClasses.Rentar import Rentar
from datetime import timedelta, datetime

renta_blueprint = Blueprint('renta', __name__, url_prefix='/renta')

@renta_blueprint.route('/') #localhost:5000/renta/
def index_rentas():
    return render_template('renta.html')

@renta_blueprint.route('/consultar') #localhost:5000/renta/consultar
def ver_rentas():
    # Recupera todas las rentas de la base de datos
    query = Rentar.query.all()
    rentas = []
    for renta in query:
        entrega = renta.fecha_renta + timedelta(days=renta.dias_de_renta)
        retraso = False
        if entrega < datetime.now() and not renta.estatus:
            retraso = True
        rentas.append((renta, entrega.date(), retraso))
    return render_template('read_rentas.html', rentas=rentas)

@renta_blueprint.route('/actualizar', methods=['GET', 'POST']) #localhost:5000/renta/actualizar
def actualizar_renta():
    if request.method == 'POST':
        try:
            renta_id = request.form['id']
            # Redirige a la vista de actualización con el ID de la renta proporcionado
            return redirect(url_for('renta.actualizar_datos', renta_id=renta_id))
        except Exception as e:
            db.session.rollback()
            flash('No se pudo actualizar la renta', 'error')
            return render_template('update_renta.html')
    return render_template('update_renta.html')

@renta_blueprint.route('/actualizar/<int:renta_id>', methods=['GET', 'POST'])
def actualizar_datos(renta_id):
    renta = Rentar.query.get(renta_id)
    if renta is None:
        flash('No se encontró la renta', 'error')
        return redirect(url_for('renta.actualizar_renta'))
    if request.method == 'POST':
        try:
            # Actualiza los datos de la renta
            renta.estatus = request.form.get('estatus') is not None
            db.session.commit()
            return render_template('renta.html')
        except Exception as e:
            db.session.rollback()
            flash('No se pudo actualizar la renta', 'error')
            return render_template('updating_renta.html', renta = renta)
    return render_template('updating_renta.html', renta = renta)

@renta_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_renta():
    if request.method == 'GET':
        return render_template('add_renta.html')
    else:
        try:
            #Obtengo la información del método post.
            idUsuario = request.form['idUsuario']
            idPelicula = request.form['idPelicula']
            fecha_renta = request.form.get('fecha_renta')
            dias_de_renta = request.form['dias']
            #Creo mi renta.
            renta = Rentar(idUsuario, idPelicula, fecha_renta, dias_de_renta, False)
            #Lo guardo en la DB
            db.session.add(renta)
            db.session.commit()
            # Redirijo a la vista principal.
            return render_template('renta.html')
        except Exception as e:
            db.session.rollback()
            flash('No se pudo agregar la renta', 'error')
            return render_template('add_renta.html')