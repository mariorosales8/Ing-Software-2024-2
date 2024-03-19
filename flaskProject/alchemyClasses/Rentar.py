from sqlalchemy import Boolean
from alchemyClasses import db
from sqlalchemy import Column, Integer, ForeignKey, DateTime


class Rentar(db.Model):
    __tablename__ = 'rentar'
    idRentar = Column(Integer, primary_key=True)
    idUsuario = Column(Integer, ForeignKey('usuarios.idUsuario', ondelete='CASCADE'))
    idPelicula = Column(Integer, ForeignKey('peliculas.idPelicula', ondelete='CASCADE'))
    fecha_renta = Column(DateTime)
    dias_de_renta = Column(Integer, default=5)
    estatus = Column(Boolean, default=False)

    def __init__(self, idUsuario, idPelicula, fecha_renta, dias_de_renta=5, estatus=False):
        self.idUsuario = idUsuario
        self.idPelicula = idPelicula
        self.fecha_renta = fecha_renta
        self.dias_de_renta = dias_de_renta
        self.estatus = estatus

    def __str__(self):
        return f'ID_Renta: {self.idRentar}, ID_Usuario: {self.idUsuario}, ID_Pelicula: {self.idPelicula}'