from sqlalchemy import Column, Integer, String, Boolean, LargeBinary
from alchemyClasses import db


class Usuario(db.Model):
    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, primary_key=True)
    nombre = Column(String(64))
    apPat = Column(String(64))
    apMat = Column(String(64))
    password = Column(String(64))
    email = Column(String(64), unique=True, default=None)
    profilePicture = Column(LargeBinary)
    superUser = Column(Boolean, default=None)

    def __init__(self, nombre, apPat, apMat, password, email, profilePicture=None, superUser=False):
        self.nombre = nombre
        self.apPat = apPat
        self.apMat = apMat
        self.password = password
        self.email = email
        self.profilePicture = profilePicture
        self.superUser = superUser

    def __str__(self):
        return f'Usuario: {self.nombre} {self.apPat} {self.apMat}, ID: : {self.idUsuario}, Email: {self.email}'
