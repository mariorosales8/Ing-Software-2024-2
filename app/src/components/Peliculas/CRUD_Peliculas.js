import React from "react";
import './CRUD_Peliculas.css';
import Pelicula_C from "./C/Pelicula_C";
import Pelicula_R from "./R/Pelicula_R";


const Peliculas = () => {
    const [lista_peliculas, setLista_peliculas] = React.useState([
        {
            nombre: 'El Padrino',
            genero: 'Drama',
            duracion: 175,
            inventario: 5
        },
        {
            nombre: 'El Señor de los Anillos',
            genero: 'Fantasía',
            duracion: 201,
            inventario: 3
        },
        {
            nombre: 'El Rey León',
            genero: 'Animación',
            duracion: 88,
            inventario: 7
        }
    ]);

    const agregaPelicula = (pelicula) => {
        lista_peliculas.push(pelicula);
        setLista_peliculas([...lista_peliculas]);
    };
    const borraPelicula = (nombre, genero, duracion, inventario) => {
        const nuevaLista = lista_peliculas.filter(pelicula =>
            pelicula.nombre !== nombre && pelicula.genero !== genero && pelicula.duracion !== duracion && pelicula.inventario !== inventario
        );
        setLista_peliculas(nuevaLista);
    };
    const actualizaPelicula = (actualizado, nombre, genero, duracion, inventario) => {
        const nuevaLista = lista_peliculas.map(pelicula =>
            pelicula.nombre === nombre && pelicula.genero === genero && pelicula.duracion === duracion && pelicula.inventario === inventario ?
                actualizado : pelicula
        );
        setLista_peliculas(nuevaLista);
    }

    const [update, setUpdate] = React.useState(null);

    return (
        <div>
            <div>
                <a href="/">
                  <button className="agregar-pelicula-btn">Volver al Inicio</button>
                </a>
            </div>
            <div className="Peliculas">
              <h1>Clonbuster</h1>
                <h2>Peliculas</h2>
                <Pelicula_C agregaPelicula={agregaPelicula} update={update} setUpdate={setUpdate} actualizaPelicula={actualizaPelicula} />
                <Pelicula_R peliculas={lista_peliculas} borraPelicula={borraPelicula} setUpdate={setUpdate} />
            </div>
        </div>
    );
}

export default Peliculas;