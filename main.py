from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Base de datos simulada para usuarios y tareas
database_users = []
database_tasks = []


class User(BaseModel):
    username: str
    email: str
    password: str


class Task(BaseModel):
    title: str
    description: str
    status: str


# Registro de Usuarios
@app.post("/register")
async def register_user(user: User):
    database_users.append(user)
    return {"message": "Usuario registrado exitosamente"}


# Obtener Datos de Usuario
@app.get("/user/{user_id}")
async def get_user(user_id: int):
    if user_id < 0 or user_id >= len(database_users):
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return database_users[user_id]


# Crear Tareas
@app.post("/tasks/create")
async def create_task(task: Task):
    database_tasks.append(task)
    return {"message": "Tarea creada exitosamente"}


# Listar Tareas por Usuario
@app.get("/tasks/{user_id}")
async def get_tasks(user_id: int):
    tasks = [task for task in database_tasks if task.user_id == user_id]
    return tasks