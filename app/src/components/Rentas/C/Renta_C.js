import React, { useEffect, useState } from 'react';

const Renta_C = ({ agregaRenta, update, setUpdate, actualizaRenta }) => {
    const [formData, setFormData] = useState({
        idUsuario: 0,
        idPelicula: 0,
        fecha_renta: '',
        dias_de_renta: '',
        estatus: false
    });

    useEffect(() => {
        if (update !== null) {
            setFormData({
                idUsuario: update.idUsuario,
                idPelicula: update.idPelicula,
                fecha_renta: update.fecha_renta,
                dias_de_renta: update.dias_de_renta,
                estatus: update.estatus
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
            agregaRenta(formData);
            setFormData({
                idUsuario: 0,
                idPelicula: 0,
                fecha_renta: '',
                dias_de_renta: '',
                estatus: false
            });
            setUpdate(null);
        } catch (error) {
            console.error(error);            
            alert('Error al agregar renta');
        }
    };

    const actualiza = () => {
        try {
            actualizaRenta(formData, update.idUsuario, update.idPelicula);
            setFormData({
                idUsuario: 0,
                idPelicula: 0,
                fecha_renta: '',
                dias_de_renta: '',
                estatus: false
            });
            setUpdate(null);
        }
        catch (error) {
            console.error(error);
            alert('Error al actualizar renta');
        }
    }

    return (
        <div>
            <h3>Agregar Renta</h3>
            <form onSubmit={handleSubmit}>
                <div className="agregar-renta-form">
                    <label htmlFor="idUsuario">ID Usuario:</label>
                    <input type="number" id="idUsuario" name="idUsuario" value={formData.idUsuario} onChange={handleChange} />
                </div>
                <div className="agregar-renta-form">
                    <label htmlFor="idPelicula">ID Película:</label>
                    <input type="number" id="idPelicula" name="idPelicula" value={formData.idPelicula} onChange={handleChange} />
                </div>
                <div className="agregar-renta-form">
                    <label htmlFor="fecha_renta">Fecha de Renta:</label>
                    <input type="date" id="fecha_renta" name="fecha_renta" value={formData.fecha_renta} onChange={handleChange} />
                </div>
                <div className="agregar-renta-form">
                    <label htmlFor="dias_de_renta">Días de Renta:</label>
                    <input type="number" id="dias_de_renta" name="dias_de_renta" value={formData.dias_de_renta} onChange={handleChange} />
                </div>
                <div className="agregar-renta-form">
                    <input className="superUser-checkbox" type="checkbox" id="estatus" name="estatus" checked={formData.estatus} onChange={handleChange} />
                    <label htmlFor="estatus">Entregado</label>
                </div>
                <button className='agregar-renta-btn' type="submit">Agregar Renta</button>

                {update !== null && <button className='agregar-renta-btn' type="button" onClick={actualiza}>Actualizar</button>}
            </form>
        </div>
    );
};

export default Renta_C;
