import React from 'react';
import { Link } from 'react-router-dom';
import './inicio.css';

const Inicio = () => {
    return (
        <div className='inicio-container'>
            <h1>Clonbuster</h1>
            <Link to="/clientes">
                <button className="inicio-btn">Clientes</button>
            </Link>
            <Link to="/peliculas">
                <button className="inicio-btn">Peliculas</button>
            </Link>
            <Link to="/rentas">
                <button className="inicio-btn">Rentas</button>
            </Link>
        </div>
    );
};

export default Inicio;
