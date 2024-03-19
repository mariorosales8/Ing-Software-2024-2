from flask import Blueprint, request, render_template, flash, url_for, redirect
from random import randint
from alchemyClasses import db
from alchemyClasses.Usuario import Usuario

usuario_blueprint = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario_blueprint.route('/') #localhost:5000/usuario/
def index_usuarios():
    return render_template('user.html')

@usuario_blueprint.route('/consultar') #localhost:5000/usuario/consultar
def ver_usuarios():
    # Recupera todos los usuarios de la base de datos
    usuarios = Usuario.query.all()
    return render_template('read_users.html', usuarios=usuarios)

@usuario_blueprint.route('/eliminar', methods=['GET', 'POST'])#responde a localhost:5000/usuario/eliminar
def borrar_usuario():
    if request.method == 'GET':
        return render_template('delete_user.html')
    else:
        try:
            #Busco el usuario por su id
            id_usuario = request.form['id']
            usuario = Usuario.query.get(id_usuario)
            #Lo elimino de la base de datos
            db.session.delete(usuario)
            db.session.commit()
            # Redirijo a la vista principal.
            return render_template('user.html')
        except Exception as e:
            db.session.rollback()
            flash('No se pudo eliminar el usuario', 'error')
            return render_template('delete_user.html')

@usuario_blueprint.route('/actualizar', methods=['GET', 'POST']) #localhost:5000/usuario/actualizar
def actualizar_usuario():
    if request.method == 'POST':
        try:
            usuario_id = request.form['id']
            # Redirige a la vista de actualización con el ID del usuario proporcionado
            return redirect(url_for('usuario.actualizar_datos', usuario_id=usuario_id))
        except Exception as e:
            db.session.rollback()
            flash('No se pudo actualizar el usuario', 'error')
            return render_template('update_user.html')
    return render_template('update_user.html')

@usuario_blueprint.route('/actualizar/<int:usuario_id>', methods=['GET', 'POST'])
def actualizar_datos(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    if usuario is None:
        flash('No se encontró el usuario', 'error')
        return redirect(url_for('usuario.actualizar_usuario'))
    if request.method == 'POST':
        try:
            # Actualiza los datos del usuario
            usuario.nombre = request.form['name'].encode('utf-8')
            usuario.apPat = request.form['ap_pat'].encode('utf-8')
            usuario.apMat = request.form['ap_mat'].encode('utf-8')
            usuario.password = request.form['passwd'].encode('utf-8')
            usuario.email = request.form['email'].encode('utf-8')
            usuario.superUser = request.form.get('superUser') is not None
            db.session.commit()
            return render_template('user.html')
        except Exception as e:
            db.session.rollback()
            flash('No se pudo actualizar el usuario', 'error')
            return render_template('updating_user.html', usuario=usuario)
    return render_template('updating_user.html', usuario=usuario)

@usuario_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'GET':
        return render_template('add_user.html')
    else:
        try:
            #Obtengo la información del método post.
            name = request.form['name'].encode('utf-8')
            ap_pat = request.form['ap_pat'].encode('utf-8')
            ap_mat = request.form['ap_mat'].encode('utf-8')
            passwd = request.form['passwd'].encode('utf-8')
            email = request.form['email'].encode('utf-8')
            superUser = request.form.get('superUser') is not None
            #Creo mi usuario.
            usuario = Usuario(name, ap_pat, ap_mat, passwd, email, None, superUser)
            #Lo guardo en la DB
            db.session.add(usuario)
            db.session.commit()

            # Redirijo a la vista principal.
            return render_template('user.html')

        except Exception as e:
            db.session.rollback()
            flash('No se pudo agregar el usuario', 'error')
            return render_template('add_user.html')