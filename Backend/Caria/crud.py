from sqlalchemy.orm import Session
from . import models, schemas

# --------- Crear Motor ---------
def create_motor(db: Session, motor: schemas.MotorCreate):
    db_motor = models.Motor(
        nro_serie=motor.nro_serie,
        nombre_motor=motor.nombre_motor,
        potencia=motor.potencia,
        tipo_combustible=motor.tipo_combustible,
        velocidad=motor.velocidad,
        rendimiento=motor.rendimiento
    )
    db.add(db_motor)
    db.commit()
    db.refresh(db_motor)
    return db_motor

# --------- Crear Neumaticos ---------
def create_neumatico(db: Session, neumatico: schemas.NeumaticosCreate):
    db_neumatico = models.Neumaticos(
        tipo_neumaticos=neumatico.tipo_neumaticos,
        anchura=neumatico.anchura,
        altura=neumatico.altura,
        capacidad_carga=neumatico.capacidad_carga,
        velocidad_maxima=neumatico.velocidad_maxima,
        diametro=neumatico.diametro,
        radial=neumatico.radial
    )
    db.add(db_neumatico)
    db.commit()
    db.refresh(db_neumatico)
    return db_neumatico

# --------- Crear Frenos ---------
def create_freno(db: Session, freno: schemas.FrenosCreate):
    db_freno = models.Frenos(
        tipo_freno=freno.tipo_freno,
        tipo_pedal=freno.tipo_pedal,
        tipo_bomba=freno.tipo_bomba,
        tipo_liquido=freno.tipo_liquido,
        tipo_pastilla=freno.tipo_pastilla,
        tipo_disco=freno.tipo_disco,
        tipo_pinza=freno.tipo_pinza,
        tipo_tambor=freno.tipo_tambor
    )
    db.add(db_freno)
    db.commit()
    db.refresh(db_freno)
    return db_freno

# --------- Crear Coche ---------
def create_coche(db: Session, coche: schemas.CochesCreate):
    db_coche = models.Coche(
        modelo=coche.modelo,
        marca=coche.marca,
        motor_id=coche.motor_id,
        cambio=coche.cambio,
        color=coche.color,
        plazas=coche.plazas,
        consumo=coche.consumo,
        neumatico_id=coche.neumatico_id,
        freno_id=coche.freno_id
    )
    db.add(db_coche)
    db.commit()
    db.refresh(db_coche)
    return db_coche

# --------- Obtener todos los Coches ---------
def get_coches(db: Session):
    return db.query(models.Coche).all()

# --------- Obtener Coche por ID ---------
def get_coche(db: Session, coche_id: int):
    return db.query(models.Coche).filter(models.Coche.id == coche_id).first()

# --------- Obtener los Motores de un Coche ---------
def get_motores(db: Session, coche_id: int):
    coche = db.query(models.Coche).filter(models.Coche.id == coche_id).first()
    if coche:
        return coche.motor  # Devuelve el motor asociado al coche
    return None

# --------- Obtener los Neumaticos de un Coche ---------
def get_neumaticos(db: Session, coche_id: int):
    coche = db.query(models.Coche).filter(models.Coche.id == coche_id).first()
    if coche:
        return coche.neumaticos  # Devuelve los neumáticos asociados al coche
    return None

# --------- Obtener los Frenos de un Coche ---------
def get_frenos(db: Session, coche_id: int):
    coche = db.query(models.Coche).filter(models.Coche.id == coche_id).first()
    if coche:
        return coche.frenos  # Devuelve los frenos asociados al coche
    return None
