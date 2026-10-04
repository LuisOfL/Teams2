from fastapi import WebSocket
import json

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except Exception:
                pass

def format_notification(client_id: str, joined: bool = True) -> str:
    text = f"{client_id} se ha conectado al canal." if joined else f"{client_id} ha abandonado la sesión."
    return json.dumps({
        "sender": "Sistema",
        "text": text,
        "type": "notification"
    })