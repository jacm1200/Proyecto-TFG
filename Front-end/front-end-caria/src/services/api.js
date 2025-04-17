
 /*Hace referencia a mi Back-end*/

const API_URL = "http://localhost:8001";

export async function getCoches() {
  const response = await fetch(`${API_URL}/coches/`);
  if (!response.ok) {
    throw new Error("No se pudo obtener la lista de coches");
  }
  return await response.json();
}

export const getMotor = async (cocheId) => {
    try {
      const response = await fetch(`${API_URL}/coches/${cocheId}/motor`);
      if (!response.ok) {
        throw new Error(`Error al obtener el motor del coche con ID ${cocheId}`);
      }
      return await response.json();  // Devuelve los detalles del motor
    } catch (error) {
      throw new Error(error.message);
    }
  };
  
  // Función para obtener los neumáticos de un coche
  export const getNeumatico = async (cocheId) => {
    try {
      const response = await fetch(`${API_URL}/coches/${cocheId}/neumaticos`);
      if (!response.ok) {
        throw new Error(`Error al obtener los neumáticos del coche con ID ${cocheId}`);
      }
      return await response.json();  // Devuelve los detalles de los neumáticos
    } catch (error) {
      throw new Error(error.message);
    }
  };
  
  // Función para obtener los frenos de un coche
  export const getFreno = async (cocheId) => {
    try {
      const response = await fetch(`${API_URL}/coches/${cocheId}/frenos`);
      if (!response.ok) {
        throw new Error(`Error al obtener los frenos del coche con ID ${cocheId}`);
      }
      return await response.json();  // Devuelve los detalles de los frenos
    } catch (error) {
      throw new Error(error.message);
    }
  };

  
export async function loginUser(username, password) {
  const response = await fetch("http://localhost:8000/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ username, password }),
  });

  if (!response.ok) {
    throw new Error("Error en el login");
  }

  return response.json(); // Esto debe devolver los datos del usuario si el login es exitoso
}
