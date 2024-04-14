import React, { useEffect, useState } from 'react';

const Cliente_C = ({ agregaUsuario, update, setUpdate, actualizaUsuario }) => {
    const [formData, setFormData] = useState({
        name: '',
        ap_pat: '',
        ap_mat: '',
        passwd: '',
        email: '',
        superUser: false
    });

    useEffect(() => {
        if (update !== null) {
            setFormData({
                name: update.name,
                ap_pat: update.ap_pat,
                ap_mat: update.ap_mat,
                passwd: update.passwd,
                email: update.email,
                superUser: update.superUser
            });
        }
    }, [update]);

    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;
        const newValue = type === 'checkbox' ? checked : value;
        setFormData({
            ...formData,
            [name]: newValue
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            agregaUsuario(formData);
            setFormData({
                name: '',
                ap_pat: '',
                ap_mat: '',
                passwd: '',
                email: '',
                superUser: false
            });
            setUpdate(null);
        } catch (error) {
            console.error(error);            
            alert('Error al agregar usuario');
        }
    };

    const actualiza = () => {
        try {
            actualizaUsuario(formData, update.name, update.ap_pat, update.ap_mat, update.email);
            setFormData({
                name: '',
                ap_pat: '',
                ap_mat: '',
                passwd: '',
                email: '',
                superUser: false
            });
            setUpdate(null);
        }
        catch (error) {
            console.error(error);
            alert('Error al actualizar usuario');
        }
    }

    return (
        <div>
            <h3>Agregar Usuario</h3>
            <form onSubmit={handleSubmit}>
                <div className="agregar-usuario-form">
                    <label htmlFor="name">Nombre:</label>
                    <input type="text" id="name" name="name" value={formData.name} onChange={handleChange} required />
                </div>
                <div className="agregar-usuario-form">
                    <label htmlFor="ap_pat">Apellido Paterno:</label>
                    <input type="text" id="ap_pat" name="ap_pat" value={formData.ap_pat} onChange={handleChange} required />
                </div>
                <div className="agregar-usuario-form">
                    <label htmlFor="ap_mat">Apellido Materno:</label>
                    <input type="text" id="ap_mat" name="ap_mat" value={formData.ap_mat} onChange={handleChange} required />
                </div>
                <div className="agregar-usuario-form">
                    <label htmlFor="passwd">Contraseña:</label>
                    <input type="password" id="passwd" name="passwd" value={formData.passwd} onChange={handleChange} required />
                </div>
                <div className="agregar-usuario-form">
                    <label htmlFor="email">Correo electrónico:</label>
                    <input type="email" id="email" name="email" value={formData.email} onChange={handleChange} required />
                </div>
                <div className="agregar-usuario-form">
                    <input className="superUser-checkbox" type="checkbox" id="superUser" name="superUser" checked={formData.superUser} onChange={handleChange} />
                    <label htmlFor="superUser">Super Usuario</label>
                </div>
                <button className='agregar-usuario-btn' type="submit">Agregar Usuario</button>

                {update !== null && <button className='agregar-usuario-btn' type="button" onClick={actualiza}>Actualizar</button>}
            </form>
        </div>
    );
};

export default Cliente_C;
