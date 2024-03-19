from sqlalchemy import Column, Integer, String
from alchemyClasses import db

class Pelicula(db.Model):
    __tablename__ = 'peliculas'
    idPelicula = Column(Integer, primary_key=True)
    nombre = Column(String(64))
    genero = Column(String(64), default=None)
    duracion = Column(Integer, default=None)
    inventario = Column(Integer, default=1)

    def __init__(self, nombre, genero=None, duracion=None, inventario=1):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.inventario = inventario

    def __str__(self):
        return f'Película: {self.nombre}, ID: {self.idPelicula}, Inventario: {self.inventario}'