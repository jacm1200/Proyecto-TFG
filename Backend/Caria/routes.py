from typing import List
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from Caria import models
from . import schemas, crud, database
from starlette.middleware.sessions import SessionMiddleware
from .schemas import UserLogin, UserResponse
from .models import User


router = APIRouter()

# --------- Crear Motor ---------
@router.post("/motores/", response_model=schemas.MotorResponse)
def crear_motor(motor: schemas.MotorCreate, db: Session = Depends(database.get_db)):
    return crud.create_motor(db=db, motor=motor)

# --------- Crear Neumatico ---------
@router.post("/neumaticos/", response_model=schemas.NeumaticosResponse)
def crear_neumatico(neumatico: schemas.NeumaticosCreate, db: Session = Depends(database.get_db)):
    return crud.create_neumatico(db=db, neumatico=neumatico)

# --------- Crear Freno ---------
@router.post("/frenos/", response_model=schemas.FrenosResponse)
def crear_freno(freno: schemas.FrenosCreate, db: Session = Depends(database.get_db)):
    return crud.create_freno(db=db, freno=freno)

# --------- Crear Coche ---------
@router.post("/coches/", response_model=schemas.CochesResponse)
def crear_coche(coche: schemas.CochesCreate, db: Session = Depends(database.get_db)):
    return crud.create_coche(db=db, coche=coche)

# --------- Obtener todos los Coches --------- FUNCIONAAAA
@router.get("/coches/", response_model=List[schemas.CochesCreate])
def get_coches(db: Session = Depends(database.get_db)):
    coches = db.query(models.Coche).all()
    return coches

# --------- Obtener Coche por ID --------- FUNCIONAAAA
@router.get("/coches/{coche_id}", response_model=schemas.CochesResponse)
def obtener_coche(coche_id: int, db: Session = Depends(database.get_db)):
    db_coche = crud.get_coche(db=db, coche_id=coche_id)
    if db_coche is None:
        raise HTTPException(status_code=404, detail="Coche no encontrado")
    return db_coche

# --------- Obtener Motor de un Coche ---------  FUNCIONAAAA
@router.get("/coches/{coche_id}/motor", response_model=schemas.MotorResponse)
def obtener_motor(coche_id: int, db: Session = Depends(database.get_db)):
    motor = crud.get_motores(db=db, coche_id=coche_id)
    if motor is None:
        raise HTTPException(status_code=404, detail="Motor no encontrado")
    return motor

# --------- Obtener Neumaticos de un Coche ---------  FUNCIONAAA
@router.get("/coches/{coche_id}/neumaticos", response_model=schemas.NeumaticosResponse)
def obtener_neumaticos(coche_id: int, db: Session = Depends(database.get_db)):
    neumaticos = crud.get_neumaticos(db=db, coche_id=coche_id)
    if neumaticos is None:
        raise HTTPException(status_code=404, detail="Neumaticos no encontrados")
    return neumaticos

# --------- Obtener Frenos de un Coche --------- FUNCIONAAA
@router.get("/coches/{coche_id}/frenos", response_model=schemas.FrenosResponse)
def obtener_frenos(coche_id: int, db: Session = Depends(database.get_db)):
    frenos = crud.get_frenos(db=db, coche_id=coche_id)
    if frenos is None:
        raise HTTPException(status_code=404, detail="Frenos no encontrados")
    return frenos



@router.post("/login", response_model=UserResponse)
def login(user: UserLogin, request: Request, db: Session = Depends(database.get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Guardar en la sesión
    request.session["user"] = {"username": db_user.username, "role": db_user.role}
    return {"username": db_user.username, "role": db_user.role}

@router.get("/me", response_model=UserResponse)
def get_me(request: Request):
    user = request.session.get("user")
    if not user:
        raise HTTPException(status_code=401, detail="Not logged in")
    return user

@router.post("/logout")
def logout(request: Request):
    request.session.clear()
    return {"message": "Logged out"}

def is_admin(request: Request):
    user = request.session.get("user")
    if not user or user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Access forbidden")
