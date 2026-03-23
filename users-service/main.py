from fastapi import FastAPI
import time

app = FastAPI()

users = {
    1: {"nome": "Carlos", "idade": 20},
    2: {"nome": "Ana", "idade": 25}
}

@app.get("/users/{id}")
def get_user(id: int):
    time.sleep(2)  # simula lentidão
    return users.get(id, {"erro": "Usuário não encontrado"})