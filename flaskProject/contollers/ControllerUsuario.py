from flask import Blueprint, request, render_template, flash, url_for
from random import randint
from alchemyClasses import db
from alchemyClasses.Usuario import Usuario

usuario_blueprint = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario_blueprint.route('/') #localhost:5000/usuario/
def ver_usuarios():
    return render_template('user.html')

#responde a localhost:5000/usuario/id/1
@usuario_blueprint.route('/id/<int:id_usuario>/<string:nombre>') #<tipo:nombre_variable>
def ver_usuario_id(id_usuario, nombre):
    return f"Se hace el query con el id {id_usuario} y el nombre {nombre}"


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