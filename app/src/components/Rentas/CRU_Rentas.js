import React from "react";
import './CRU_Rentas.css';
import Renta_C from "./C/Renta_C";
import Renta_R from "./R/Renta_R";


const Rentas = () => {
    const [lista_rentas, setLista_rentas] = React.useState([
        {
            idUsuario: 1,
            idPelicula: 1,
            fecha_renta: '2023-10-01',
            dias_de_renta: '7',
            estatus: true
        },
        {
            idUsuario: 2,
            idPelicula: 2,
            fecha_renta: '2024-02-02',
            dias_de_renta: '8',
            estatus: false
        },
        {
            idUsuario: 3,
            idPelicula: 3,
            fecha_renta: '2024-04-13',
            dias_de_renta: '2',
            estatus: false
        }
    ]);

    const agregaRenta = (renta) => {
        lista_rentas.push(renta);
        setLista_rentas([...lista_rentas]);
    };
    const borraRenta = (idUsuario, idPelicula) => {
        const nuevaLista = lista_rentas.filter(renta =>
            renta.idUsuario !== idUsuario && renta.idPelicula !== idPelicula
        );
        setLista_rentas(nuevaLista);
    };
    const actualizaRenta = (actualizado, idUsuario, idPelicula) => {
        const nuevaLista = lista_rentas.map(renta =>
            renta.idUsuario === idUsuario && renta.idPelicula === idPelicula ?
                actualizado : renta
        );
        setLista_rentas(nuevaLista);
    }

    const [update, setUpdate] = React.useState(null);

    return (
        <div>
            <div>
                <a href="/">
                  <button className="agregar-renta-btn">Volver al Inicio</button>
                </a>
            </div>
            <div className="Rentas">
              <h1>Clonbuster</h1>
                <h2>Rentas</h2>
                <Renta_C agregaRenta={agregaRenta} update={update} setUpdate={setUpdate} actualizaRenta={actualizaRenta} />
                <Renta_R rentas={lista_rentas} borraRenta={borraRenta} setUpdate={setUpdate} />
            </div>
        </div>
    );
}

export default Rentas;