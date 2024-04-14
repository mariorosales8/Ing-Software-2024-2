import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

import Inicio from "./inicio";
import Clientes from "./components/Clientes/CRUD_Clientes";
import Cliente_C from "./components/Clientes/C/Cliente_C";
// import crea_cliente from "./components/Clientes/C/crea_cliente";
import Cliente_R from "./components/Clientes/R/Cliente_R";
// import lee_cliente from "./components/Clientes/R/lee_cliente";
// import Cliente_U from "./components/Clientes/Cliente_U";
// import Cliente_D from "./components/Clientes/Cliente_D";
// import Peliculas from "./components/Peliculas/CRUD_Peliculas";
// import Pelicula_C from "./components/Peliculas/Pelicula_C";
// import Pelicula_R from "./components/Peliculas/Pelicula_R";
// import Pelicula_U from "./components/Peliculas/Pelicula_U";
// import Pelicula_D from "./components/Peliculas/Pelicula_D";
// import Rentas from "./components/Rentas/CRUD_Rentas";
// import Renta_C from "./components/Rentas/Renta_C";
// import Renta_R from "./components/Rentas/Renta_R";
// import Renta_U from "./components/Rentas/Renta_U";
// import Renta_D from "./components/Rentas/Renta_D";


function App() {
  return (
    <Router>
      <Routes>
          <Route path="/" element={<Inicio/>} />

          <Route path="/clientes" element={<Clientes/>} />
          <Route path="/cliente/create" element={<crea_cliente/>} />
          <Route path="/cliente/read" element={<lee_cliente/>} />
          
          {/* <Route path="/cliente/update" element={<Cliente_U/>} /> */}
          {/* <Route path="/cliente/delete" element={<Cliente_D/>} /> */}

          {/* <Route path="/peliculas" element={<Peliculas/>} /> */}
          {/* <Route path="/pelicula/create" element={<Pelicula_C/>} /> */}
          {/* <Route path="/pelicula/read" element={<Pelicula_R/>} /> */}
          {/* <Route path="/pelicula/update" element={<Pelicula_U/>} /> */}
          {/* <Route path="/pelicula/delete" element={<Pelicula_D/>} /> */}

          {/* <Route path="/rentas" element={<Rentas/>} /> */}
          {/* <Route path="/renta/create" element={<Renta_C/>} /> */}
          {/* <Route path="/renta/read" element={<Renta_R/>} /> */}
          {/* <Route path="/renta/update" element={<Renta_U/>} /> */}
          {/* <Route path="/renta/delete" element={<Renta_D/>} /> */}
      </Routes>
    </Router>
  );
}

export default App;
