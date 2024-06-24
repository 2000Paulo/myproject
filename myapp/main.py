from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from redis import Redis
import json
from datetime import datetime
import os

app = FastAPI()
redis = Redis(host='localhost', port=6379, db=0)

# Usar caminho absoluto para a pasta de templates
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            message = {"client_id": client_id, "message": data, "timestamp": timestamp}
            redis.rpush("chat_messages", json.dumps(message))
            await websocket.send_text(f"Mensagem enviada às {timestamp}: {data}")
    except WebSocketDisconnect:
        await websocket.close()

@app.get("/messages/")
async def get_messages():
    messages = redis.lrange("chat_messages", 0, -1)
    return [json.loads(message) for message in messages]
