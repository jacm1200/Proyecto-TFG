import { useState } from "react";
import { loginUser } from "../services/api"; // Función para manejar la solicitud al backend

export default function Navbar() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loggedIn, setLoggedIn] = useState(false);
  const [error, setError] = useState(null);

  // Función para manejar el login
  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await loginUser(username, password);
      if (response.username) {
        setLoggedIn(true);
        sessionStorage.setItem("user", JSON.stringify(response)); // Guardamos el usuario en sesión
      } else {
        setError("Credenciales incorrectas");
      }
    } catch (err) {
      setError("Error al iniciar sesión");
    }
  };

  // Función para cerrar sesión
  const handleLogout = () => {
    sessionStorage.removeItem("user");
    setLoggedIn(false);
  };

  return (
    <nav className="bg-blue-600 text-white p-4">
      <div className="max-w-7xl mx-auto flex justify-between items-center">
        <a href="/" className="text-2xl font-bold">
          <span className="text-yellow-400">Caria</span>App
        </a>

        <div className="space-x-6">
          <a href="/" className="hover:text-yellow-400 transition">Inicio</a>
          <a href="/coches" className="hover:text-yellow-400 transition">Coches</a>
          <a href="/acerca" className="hover:text-yellow-400 transition">Acerca de</a>

          {loggedIn ? (
            <>
              <span className="text-white">Bienvenido, {JSON.parse(sessionStorage.getItem("user")).username}</span>
              <button onClick={handleLogout} className="text-white hover:text-yellow-400">Cerrar sesión</button>
            </>
          ) : (
            <form onSubmit={handleLogin} className="flex items-center space-x-2">
              <input
                type="text"
                placeholder="Usuario"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                className="p-2 rounded-md"
              />
              <input
                type="password"
                placeholder="Contraseña"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="p-2 rounded-md"
              />
              <button type="submit" className="p-2 bg-yellow-400 text-black rounded-md">Login</button>
            </form>
          )}
        </div>
      </div>
      {error && <div className="text-red-500">{error}</div>}
    </nav>
  );
}
