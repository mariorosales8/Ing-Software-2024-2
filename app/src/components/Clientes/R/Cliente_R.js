import React from 'react';

const Cliente_R = ({ usuarios, borraUsuario, setUpdate }) => {
    const handleDelete = (name, ap_pat, ap_mat, email) => {
        borraUsuario(name, ap_pat, ap_mat, email);
    };
    const handleUpdate = (name, ap_pat, ap_mat, email) => {
        const updated = usuarios.filter(usuario => usuario.name === name && usuario.ap_pat === ap_pat && usuario.ap_mat === ap_mat && usuario.email === email)[0];
        setUpdate(updated);
    }


    return (
        <div>
            <h1>Lista de Usuarios</h1>
            <table>
                <thead>
                    <tr>
                        <th>Nombre</th>
                        <th>Apellido Paterno</th>
                        <th>Apellido Materno</th>
                        <th>Correo Electrónico</th>
                        <th>Super Usuario</th>
                        <th></th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    {usuarios.map(usuario => (
                        <tr key={usuario.id}>
                            <td>{usuario.name}</td>
                            <td>{usuario.ap_pat}</td>
                            <td>{usuario.ap_mat}</td>
                            <td>{usuario.email}</td>
                            <td>{usuario.superUser ? "Sí" : "No"}</td>
                            <td>
                                <button onClick={() => handleDelete(usuario.name, usuario.ap_pat, usuario.ap_mat, usuario.email)}>Borrar</button>
                            </td>
                            <td>
                                <button onClick={() => handleUpdate(usuario.name, usuario.ap_pat, usuario.ap_mat, usuario.email)}>Editar</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Cliente_R;