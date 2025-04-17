from fastapi import FastAPI
from Caria import models, database, routes
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

# Crear tablas si no existen
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permitir llamadas desde React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas
app.add_middleware(SessionMiddleware, secret_key="11111")
app.include_router(routes.router)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

