from fastapi import FastAPI
import requests

app = FastAPI()

orders = {
    1: {"produto": "Notebook", "user_id": 1},
    2: {"produto": "Mouse", "user_id": 2}
}

@app.get("/orders/{id}")
def get_order(id: int):
    order = orders.get(id)

    if not order:
        return {"erro": "Pedido não encontrado"}

    try:
        response = requests.get(
            f"http://users-service:8000/users/{order['user_id']}",
            timeout=3
        )
        user = response.json()
    except requests.exceptions.RequestException:
        return {"erro": "Falha ao comunicar com o serviço de usuários"}

    return {
        "pedido": order,
        "usuario": user
    }