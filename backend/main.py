from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import uvicorn

app = FastAPI(title="Mini Teams API")

# Schemas
class Message(BaseModel):
    user: str
    content: str

class Channel(BaseModel):
    id: str
    name: str

class CreateMessageRequest(BaseModel):
    user: str
    content: str

# Base de datos temporal en memoria
channels_db: Dict[str, str] = {
    "general": "General",
    "proyectos": "Proyectos",
    "anuncios": "Anuncios"
}

messages_db: Dict[str, List[Dict[str, str]]] = {
    "general": [
        {"user": "Alice", "content": "¡Hola a todos!"},
        {"user": "Bob", "content": "Bienvenidos al canal general."}
    ],
    "proyectos": [
        {"user": "Luis", "content": "La API ya está lista."}
    ],
    "anuncios": []
}

@app.get("/channels", response_model=List[Channel])
def get_channels():
    return [{"id": key, "name": val} for key, val in channels_db.items()]

@app.get("/channels/{channel_id}/messages", response_model=List[Message])
def get_messages(channel_id: str):
    if channel_id not in messages_db:
        raise HTTPException(status_code=404, detail="Canal no encontrado")
    return messages_db[channel_id]

@app.post("/channels/{channel_id}/messages", response_model=Message)
def post_message(channel_id: str, payload: CreateMessageRequest):
    if channel_id not in messages_db:
        raise HTTPException(status_code=404, detail="Canal no encontrado")
    new_msg = {"user": payload.user, "content": payload.content}
    messages_db[channel_id].append(new_msg)
    return new_msg

if __name__ == "__main__":
    uvicorn.run("backend:app", host="127.0.0.1", port=8000, reload=True)