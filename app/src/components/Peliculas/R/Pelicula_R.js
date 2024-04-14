import React from 'react';

const Pelicula_R = ({ peliculas, borraPelicula, setUpdate }) => {
    const handleDelete = (nombre, genero, duracion, inventario) => {
        borraPelicula(nombre, genero, duracion, inventario);
    };
    const handleUpdate = (nombre, genero, duracion, inventario) => {
        const updated = peliculas.filter(pelicula => pelicula.nombre === nombre && pelicula.genero === genero && pelicula.duracion === duracion && pelicula.inventario === inventario)[0];
        setUpdate(updated);
    }


    return (
        <div className='tabla-peliculas'>
            <h3>Lista de Películas</h3>
            <table>
                <thead>
                    <tr>
                        <th>Nombre</th>
                        <th>Genero</th>
                        <th>Duracion</th>
                        <th>Inventario</th>
                        <th></th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    {peliculas.map(pelicula => (
                        <tr key={pelicula.id}>
                            <td>{pelicula.nombre}</td>
                            <td>{pelicula.genero}</td>
                            <td>{pelicula.duracion}</td>
                            <td>{pelicula.inventario}</td>
                            <td>
                                <button onClick={() => handleDelete(pelicula.nombre, pelicula.genero, pelicula.duracion, pelicula.inventario)}>Borrar</button>
                            </td>
                            <td>
                                <button onClick={() => handleUpdate(pelicula.nombre, pelicula.genero, pelicula.duracion, pelicula.inventario)}>Editar</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Pelicula_R;