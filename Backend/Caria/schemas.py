from pydantic import BaseModel
from typing import List


class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    username: str
    role: str

    class Config:
        from_attributes = True

# --------- Motor ---------
class MotorCreate(BaseModel):
    nro_serie: str
    nombre_motor: str
    potencia: float
    tipo_combustible: str
    velocidad: float
    rendimiento: float

    class Config:
        from_attributes = True

class MotorResponse(MotorCreate):
    class Config:
        from_attributes = True


# --------- Neumáticos ---------
class NeumaticosCreate(BaseModel):
    tipo_neumaticos: str
    anchura: int
    altura: int
    capacidad_carga: int
    velocidad_maxima: int
    diametro: int
    radial: bool

    class Config:
        from_attributes = True

class NeumaticosResponse(NeumaticosCreate):
    id: int

    class Config:
        from_attributes = True


# --------- Frenos ---------
class FrenosCreate(BaseModel):
    tipo_freno: str
    tipo_pedal: str
    tipo_bomba: str
    tipo_liquido: str
    tipo_pastilla: str
    tipo_disco: str
    tipo_pinza: str
    tipo_tambor: str

    class Config:
        from_attributes = True

class FrenosResponse(FrenosCreate):
    id: int

    class Config:
        from_attributes = True


# --------- Coches ---------
class CochesCreate(BaseModel):
    id: int
    modelo: str
    marca: str
    cambio: str
    color: str
    plazas: int
    consumo: float
    motor_id: str
    neumatico_id: int
    freno_id: int

    class Config:
        from_attributes = True

class CochesResponse(CochesCreate):
    motores: List[MotorResponse]  # Lista de motores
    neumaticos: List[NeumaticosResponse]  # Lista de neumáticos
    frenos: List[FrenosResponse]  # Lista de frenos

    class Config:
        from_attributes = True
