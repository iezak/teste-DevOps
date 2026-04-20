from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}

@app.get("/funcaoTeste")
async def funcaoTeste():
    return {"teste" : True, "num_aleatorio": random.randint(0, 1000)}
