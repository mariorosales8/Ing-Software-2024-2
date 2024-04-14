import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

import Inicio from "./inicio";
import Clientes from "./components/Clientes/CRUD_Clientes";
import Peliculas from "./components/Peliculas/CRUD_Peliculas";
import Rentas from "./components/Rentas/CRU_Rentas";

function App() {
  return (
    <Router>
      <Routes>
          <Route path="/" element={<Inicio/>} />

          <Route path="/clientes" element={<Clientes/>} />

          <Route path="/peliculas" element={<Peliculas/>} />

          <Route path="/rentas" element={<Rentas/>} />
      </Routes>
    </Router>
  );
}

export default App;
