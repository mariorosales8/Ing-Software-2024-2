import React from 'react';
import { Link } from 'react-router-dom';

const Inicio = () => {
    return (
        <div>
            <h1>Clonbuster</h1>
            <Link to="/clientes">
                <button>Clientes</button>
            </Link>
            <Link to="/peliculas">
                <button>Peliculas</button>
            </Link>
            <Link to="/rentas">
                <button>Rentas</button>
            </Link>
        </div>
    );
};

export default Inicio;
