import React from "react";

import './Crea_cliente.css';
import Cliente_C from "./Cliente_C";

const Crea_cliente = (props) => {
    
    const guardaClienteHandler = (clienteIngresado) => {
        const clientes = { 
            ...clienteIngresado
        };
        props.onAgregarCliente(clientes);
    };

    return (
        <div className="nuevo-cliente">
            <Cliente_C onGuardarClientes={guardaClienteHandler} />
        </div>
    )
}

export default Crea_cliente;