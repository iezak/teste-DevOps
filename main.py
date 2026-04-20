from fastapi import FastAPI

app = FastAPI()


@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}

@app.get("/funcaoTeste")
async def funcaoTeste():
    return {"teste" : "deu certo"}

