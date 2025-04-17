import enum
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# --------- Usuarios ---------

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)

# --------- Motor ---------
class Motores(Base):
    __tablename__ = "motores"

    nro_serie = Column(String, primary_key=True, index=True)
    nombre_motor = Column(String)
    potencia = Column(Float)
    tipo_combustible = Column(String)
    velocidad = Column(Float)
    rendimiento = Column(Float)

    coches = relationship("Coche", back_populates="motor")


# --------- Neumáticos ---------
class Neumaticos(Base):
    __tablename__ = "neumaticos"

    id = Column(Integer, primary_key=True, index=True)
    tipo_neumaticos = Column(String)
    anchura = Column(Integer)
    altura = Column(Integer)
    capacidad_carga = Column(Integer)
    velocidad_maxima = Column(Integer)
    diametro = Column(Integer)
    radial = Column(Boolean)

    coches = relationship("Coche", back_populates="neumaticos")


# --------- Frenos ---------
class Frenos(Base):
    __tablename__ = "frenos"

    id = Column(Integer, primary_key=True, index=True)
    tipo_freno = Column(String)
    tipo_pedal = Column(String)
    tipo_bomba = Column(String)
    tipo_liquido = Column(String)
    tipo_pastilla = Column(String)
    tipo_disco = Column(String)
    tipo_pinza = Column(String)
    tipo_tambor = Column(String)

    coches = relationship("Coche", back_populates="frenos")


# --------- Coches ---------
class Coche(Base):
    __tablename__ = "coches"

    id = Column(Integer, primary_key=True, index=True)
    modelo = Column(String)
    marca = Column(String)
    motor_id = Column(String, ForeignKey("motores.nro_serie"))
    cambio = Column(String)
    color = Column(String)
    plazas = Column(Integer)
    consumo = Column(Float)
    neumatico_id = Column(Integer, ForeignKey("neumaticos.id"))
    freno_id = Column(Integer, ForeignKey("frenos.id"))

    motor = relationship("Motores", back_populates="coches")
    neumaticos = relationship("Neumaticos", back_populates="coches")
    frenos = relationship("Frenos", back_populates="coches")

