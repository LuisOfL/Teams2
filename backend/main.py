from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import json
from utils import ConnectionManager, format_notification

app = FastAPI(title="Teams Clone Backend", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

manager = ConnectionManager()

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket)
    await manager.broadcast(format_notification(client_id, joined=True))
    try:
        while True:
            data = await websocket.receive_text()
            message_data = json.loads(data)
            message_data["sender"] = client_id
            await manager.broadcast(json.dumps(message_data))
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(format_notification(client_id, joined=False))