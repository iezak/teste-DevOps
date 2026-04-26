from fastapi import FastAPI
import random

app = FastAPI()

class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool

@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}

@app.get("/funcaoTeste")
async def funcaoTeste():
    return {"teste" : True, "num_aleatorio": random.randint(0, 1000)}


@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante

@app.put("/estudantes/update/{id_estudante}")
async def update_estudante(id_estudante: int):
    return id.estudante > 0

@app.put("/estudantes/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
    return id.estudante > 0
