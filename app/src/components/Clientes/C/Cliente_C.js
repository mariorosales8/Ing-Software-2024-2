import React, { useState } from 'react';

const Cliente_C = () => {
    const [formData, setFormData] = useState({
        name: '',
        ap_pat: '',
        ap_mat: '',
        passwd: '',
        email: '',
        superUser: false
    });

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
            const response = await fetch('/api/agregar_usuario', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });
            if (response.ok) {
                // Redirigir a la vista anterior
                window.location.href = '/clientes';
            } else {
                throw new Error('Error al agregar usuario');
            }
        } catch (error) {
            console.error(error);            
            alert('Error al agregar usuario');
        }
    };

    return (
        <div>
            <h1>Agregar Usuario</h1>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="name">Nombre:</label>
                    <input type="text" id="name" name="name" value={formData.name} onChange={handleChange} required />
                </div>
                <div>
                    <label htmlFor="ap_pat">Apellido Paterno:</label>
                    <input type="text" id="ap_pat" name="ap_pat" value={formData.ap_pat} onChange={handleChange} required />
                </div>
                <div>
                    <label htmlFor="ap_mat">Apellido Materno:</label>
                    <input type="text" id="ap_mat" name="ap_mat" value={formData.ap_mat} onChange={handleChange} required />
                </div>
                <div>
                    <label htmlFor="passwd">Contraseña:</label>
                    <input type="password" id="passwd" name="passwd" value={formData.passwd} onChange={handleChange} required />
                </div>
                <div>
                    <label htmlFor="email">Correo electrónico:</label>
                    <input type="email" id="email" name="email" value={formData.email} onChange={handleChange} required />
                </div>
                <div>
                    <input type="checkbox" id="superUser" name="superUser" checked={formData.superUser} onChange={handleChange} />
                    <label htmlFor="superUser">Super Usuario</label>
                </div>
                <button type="submit">Agregar Usuario</button>
            </form>
        </div>
    );
};

export default Cliente_C;
