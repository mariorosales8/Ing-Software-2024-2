import React, { useEffect, useState } from 'react';

const Pelicula_C = ({ agregaPelicula, update, setUpdate, actualizaPelicula }) => {
    const [formData, setFormData] = useState({
        nombre: '',
        genero: '',
        duracion: 0,
        inventario: 0
    });

    useEffect(() => {
        if (update !== null) {
            setFormData({
                nombre: update.nombre,
                genero: update.genero,
                duracion: update.duracion,
                inventario: update.inventario
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
            agregaPelicula(formData);
            setFormData({
                nombre: '',
                genero: '',
                duracion: 0,
                inventario: 0
            });
            setUpdate(null);
        } catch (error) {
            console.error(error);            
            alert('Error al agregar la película');
        }
    };

    const actualiza = () => {
        try {
            actualizaPelicula(formData, update.nombre, update.genero, update.duracion, update.inventario);
            setFormData({
                nombre: '',
                genero: '',
                duracion: 0,
                inventario: 0
            });
            setUpdate(null);
        }
        catch (error) {
            console.error(error);
            alert('Error al actualizar la película');
        }
    }

    return (
        <div>
            <h3>Agregar Película</h3>
            <form onSubmit={handleSubmit}>
                <div className='agregar-pelicula-form'>
                    <label>Nombre</label>
                    <input type="text" name="nombre" value={formData.nombre} onChange={handleChange} />
                </div>
                <div className='agregar-pelicula-form'>
                    <label>Genero</label>
                    <input type="text" name="genero" value={formData.genero} onChange={handleChange} />
                </div>
                <div className='agregar-pelicula-form'>
                    <label>Duración</label>
                    <input type="number" name="duracion" value={formData.duracion} onChange={handleChange} />
                    <span>minutos</span>
                </div>
                <div className='agregar-pelicula-form'>
                    <label>Inventario</label>
                    <input type="number" name="inventario" value={formData.inventario} onChange={handleChange} />
                </div>
                <button className='agregar-pelicula-btn' type="submit">Agregar Película</button>

                {update !== null && <button className='agregar-pelicula-btn' type="button" onClick={actualiza}>Actualizar</button>}
            </form>
        </div>
    );
};

export default Pelicula_C;
