import React from 'react';

const Renta_R = ({ rentas, borraRenta, setUpdate }) => {
    const handleDelete = (idUsuario, idPelicula) => {
        borraRenta(idUsuario, idPelicula);
    };
    const handleUpdate = (idUsuario, idPelicula) => {
        const updated = rentas.filter(renta => renta.idUsuario === idUsuario && renta.idPelicula === idPelicula)[0];
        setUpdate(updated);
    }


    return (
        <div className='tabla-rentas'>
            <h3>Lista de Rentas</h3>
            <table>
                <thead>
                    <tr>
                        <th>Id Usuario</th>
                        <th>Id Película</th>
                        <th>Fecha de Renta</th>
                        <th>Días de Renta</th>
                        <th>Estatus</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    {rentas.map(renta => (
                        <tr key={renta.id}>
                            <td>{renta.idUsuario}</td>
                            <td>{renta.idPelicula}</td>
                            <td>{renta.fecha_renta}</td>
                            <td>{renta.dias_de_renta}</td>
                            <td>{renta.estatus ? "Sí" : "No"}</td>
                            <td>
                                <button onClick={() => handleUpdate(renta.idUsuario, renta.idPelicula)}>Editar</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Renta_R;