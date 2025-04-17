import { useEffect, useState } from "react";
import { getCoches, getMotor, getNeumatico, getFreno } from "../services/api";

export default function CarList() {
  const [coches, setCoches] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [search, setSearch] = useState("");
  const [filteredCoches, setFilteredCoches] = useState([]);
  const [componentDetails, setComponentDetails] = useState({});
  const [visibleDetails, setVisibleDetails] = useState({});

  useEffect(() => {
    getCoches()
      .then((data) => {
        console.log("Datos recibidos de coches:", data);  // Verificar los datos
        setCoches(data);
        setFilteredCoches(data);
      })
      .catch((err) => {
        console.error("Error al obtener los coches:", err);  // Ver si hay error
        setError(err.message);
      })
      .finally(() => {
        console.log("Cargando coches completado");  // Ver que se llega a finalmente
        setLoading(false);
      });
  }, []);
  

  useEffect(() => {
    setFilteredCoches(
      coches.filter(
        (coche) =>
          coche.modelo.toLowerCase().includes(search.toLowerCase()) ||
          coche.marca.toLowerCase().includes(search.toLowerCase())
      )
    );
  }, [search, coches]);

  const toggleComponentDetails = async (cocheId) => {
    setVisibleDetails((prev) => ({
      ...prev,
      [cocheId]: !prev[cocheId],
    }));

    if (!componentDetails[cocheId]) {
      try {
        const [motor, neumatico, freno] = await Promise.all([
          getMotor(cocheId),
          getNeumatico(cocheId),
          getFreno(cocheId),
        ]);

        setComponentDetails((prevDetails) => ({
          ...prevDetails,
          [cocheId]: { motor, neumatico, freno },
        }));
      } catch (error) {
        console.error(`Error al obtener detalles del coche ${cocheId}:`, error);
      }
    }
  };

  if (loading)
    return <p className="text-center mt-10 text-gray-600">Cargando coches...</p>;
  if (error)
    return <p className="text-center mt-10 text-red-600">Error: {error}</p>;

  return (
    <div className="p-6 max-w-6xl mx-auto">
      <h2 className="text-3xl font-bold mb-6 text-gray-800 text-center">
        Lista de Coches
      </h2>

      <input
        type="text"
        className="w-full p-2 border border-gray-300 rounded-md mb-6"
        placeholder="Buscar por modelo o marca..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

      <div className="grid gap-6 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
        {filteredCoches.length === 0 ? (
          <p className="text-center text-gray-600">No se encontraron coches.</p>
        ) : (
          filteredCoches.map((coche) => (
            <div
              key={coche.id}
              className="bg-white shadow-md rounded-lg p-5 border border-gray-200 hover:shadow-xl transition"
            >
              <h3 className="text-xl font-semibold text-indigo-600 mb-2">
                {coche.modelo}
              </h3>
              <p className="text-gray-700 mb-1">
                <strong>Marca:</strong> {coche.marca}
              </p>
              <p className="text-gray-700 mb-1">
                <strong>Cambio:</strong> {coche.cambio}
              </p>
              <p className="text-gray-700 mb-1">
                <strong>Color:</strong> {coche.color}
              </p>
              <p className="text-gray-700 mb-1">
                <strong>Plazas:</strong> {coche.plazas}
              </p>
              <p className="text-gray-700 mb-1">
                <strong>Consumo:</strong> {coche.consumo} L/100km
              </p>

              <div className="mt-4">
                <button
                  onClick={() => toggleComponentDetails(coche.id)}
                  className="bg-blue-500 text-white p-2 rounded-md"
                >
                  {visibleDetails[coche.id]
                    ? "Ocultar detalles"
                    : "Ver detalles"}
                </button>

                {visibleDetails[coche.id] && componentDetails[coche.id] && (
                  <div className="mt-4">
                    <h4 className="text-lg font-semibold text-indigo-600">
                      Detalles del Coche
                    </h4>

                    {/* Motor */}
                    {componentDetails[coche.id].motor && (
                      <div>
                        <h5 className="font-semibold text-gray-800">Motor:</h5>
                        <p>
                          <strong>Nombre:</strong>{" "}
                          {componentDetails[coche.id].motor.nombre_motor}
                        </p>
                        <p>
                          <strong>Potencia:</strong>{" "}
                          {componentDetails[coche.id].motor.potencia} HP
                        </p>
                        <p>
                          <strong>Tipo de Combustible:</strong>{" "}
                          {componentDetails[coche.id].motor.tipo_combustible}
                        </p>
                        <p>
                          <strong>Velocidad máxima:</strong>{" "}
                          {componentDetails[coche.id].motor.velocidad} km/h
                        </p>
                        <p>
                          <strong>Rendimiento:</strong>{" "}
                          {componentDetails[coche.id].motor.rendimiento} km/L
                        </p>
                      </div>
                    )}

                    {/* Neumáticos */}
                    {componentDetails[coche.id].neumatico && (
                      <div className="mt-4">
                        <h5 className="font-semibold text-gray-800">
                          Neumáticos:
                        </h5>
                        <p>
                          <strong>Tipo:</strong>{" "}
                          {componentDetails[coche.id].neumatico.tipo_neumaticos}
                        </p>
                        <p>
                          <strong>Anchura:</strong>{" "}
                          {componentDetails[coche.id].neumatico.anchura} mm
                        </p>
                        <p>
                          <strong>Altura:</strong>{" "}
                          {componentDetails[coche.id].neumatico.altura} mm
                        </p>
                        <p>
                          <strong>Capacidad de carga:</strong>{" "}
                          {componentDetails[coche.id].neumatico.capacidad_carga}{" "}
                          kg
                        </p>
                        <p>
                          <strong>Velocidad máxima:</strong>{" "}
                          {
                            componentDetails[coche.id].neumatico
                              .velocidad_maxima
                          }{" "}
                          km/h
                        </p>
                        <p>
                          <strong>Diámetro:</strong>{" "}
                          {componentDetails[coche.id].neumatico.diametro}{" "}
                          pulgadas
                        </p>
                        <p>
                          <strong>Radial:</strong>{" "}
                          {componentDetails[coche.id].neumatico.radial
                            ? "Sí"
                            : "No"}
                        </p>
                      </div>
                    )}

                    {/* Frenos */}
                    {componentDetails[coche.id].freno && (
                      <div className="mt-4">
                        <h5 className="font-semibold text-gray-800">Frenos:</h5>
                        <p>
                          <strong>Tipo de Freno:</strong>{" "}
                          {componentDetails[coche.id].freno.tipo_freno}
                        </p>
                        <p>
                          <strong>Tipo de Pedal:</strong>{" "}
                          {componentDetails[coche.id].freno.tipo_pedal}
                        </p>
                        <p>
                          <strong>Tipo de Bomba:</strong>{" "}
                          {componentDetails[coche.id].freno.tipo_bomba}
                        </p>
                        <p>
                          <strong>Tipo de Líquido:</strong>{" "}
                          {componentDetails[coche.id].freno.tipo_liquido}
                        </p>
                        <p>
                          <strong>Tipo de Pastilla:</strong>{" "}
                          {componentDetails[coche.id].freno.tipo_pastilla}
                        </p>
                        <p>
                          <strong>Tipo de Disco:</strong>{" "}
                          {componentDetails[coche.id].freno.tipo_disco}
                        </p>
                        <p>
                          <strong>Tipo de Pinza:</strong>{" "}
                          {componentDetails[coche.id].freno.tipo_pinza}
                        </p>
                        <p>
                          <strong>Tipo de Tambor:</strong>{" "}
                          {componentDetails[coche.id].freno.tipo_tambor}
                        </p>
                      </div>
                    )}
                  </div>
                )}
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}
