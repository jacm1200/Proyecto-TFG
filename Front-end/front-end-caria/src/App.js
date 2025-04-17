import React from "react";
import CarList from "./components/lista_coches";
import Navbar from "./components/navbar"; 

function App() {
  return (
    <div className="App">
      <Navbar />
      <CarList />
    </div>
  );
}

export default App;
