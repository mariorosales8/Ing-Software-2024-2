import React from "react";
import './CRUD_Clientes.css';
import Cliente_C from "./C/Cliente_C";
import Cliente_R from "./R/Cliente_R";


const Clientes = () => {
    const [lista_usuarios, setLista_usuarios] = React.useState([
        {
            name: 'Juan',
            ap_pat: 'Perez',
            ap_mat: 'Gonzalez',
            passwd: '1234',
            email: 'juan@gonz.com',
            superUser: false
        },
        {
            name: 'María',
            ap_pat: 'Gomez',
            ap_mat: 'Perez',
            passwd: '4321',
            email: 'mar@gomez.com',
            superUser: false
        },
        {
            name: 'Pedro',
            ap_pat: 'Ramirez',
            ap_mat: 'Gomez',
            passwd: '5678',
            email: 'pedr@ram.com',
            superUser: false
        }
    ]);

    const agregaUsuario = (usuario) => {
        lista_usuarios.push(usuario);
        setLista_usuarios([...lista_usuarios]);
    };
    const borraUsuario = (name, ap_pat, ap_mat, email) => {
        const nuevaLista = lista_usuarios.filter(usuario =>
            usuario.name !== name && usuario.ap_pat !== ap_pat && usuario.ap_mat !== ap_mat && usuario.email !== email
        );
        setLista_usuarios(nuevaLista);
    };
    const actualizaUsuario = (actualizado, name, ap_pat, ap_mat, email) => {
        const nuevaLista = lista_usuarios.map(usuario =>
            usuario.name === name && usuario.ap_pat === ap_pat && usuario.ap_mat === ap_mat && usuario.email === email ?
                actualizado : usuario
        );
        setLista_usuarios(nuevaLista);
    }

    const [update, setUpdate] = React.useState(null);

    return (
        <div>
            <div>
                <a href="/">
                  <button className="agregar-usuario-btn">Volver al Inicio</button>
                </a>
            </div>
            <div className="Clientes">
              <h1>Clonbuster</h1>
                <h2>Clientes</h2>
                <Cliente_C agregaUsuario={agregaUsuario} update={update} setUpdate={setUpdate} actualizaUsuario={actualizaUsuario} />
                <Cliente_R usuarios={lista_usuarios} borraUsuario={borraUsuario} setUpdate={setUpdate} />
            </div>
        </div>
    );
}

export default Clientes;