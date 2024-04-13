import React from "react";
import { Link } from "react-router-dom";
import './CRUD_Clientes.css';


const Clientes = () => {
    return (
        <div className="Clientes">
          <h1>Clonbuster</h1>
            <h2>Clientes</h2>
            <Link to="/cliente/create">
                <button>Agregar Cliente</button>
            </Link>
            <Link to="/cliente/read">
                <button>Consultar Cliente</button>
            </Link>
            <Link to="/cliente/update">
                <button>Actualizar Cliente</button>
            </Link>
            <Link to="/cliente/delete">
                <button>Eliminar Cliente</button>
            </Link>
        </div>
    );
}

export default Clientes;