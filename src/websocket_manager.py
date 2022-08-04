from typing import List, Union
from fastapi import WebSocket


class WebsocketManager:
    """WebSocket连接管理器"""

    def __init__(self):
        self.active_connections: List[WebSocket] = []  # 存活连接

    async def connect(self, websocket: WebSocket) -> None:
        await websocket.accept()  # 接受连接
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket) -> None:
        self.active_connections.remove(websocket)

    @staticmethod
    async def send_message(conn: WebSocket, message: Union[list, str, bytes, dict]):
        if isinstance(message, (dict, list)):
            return await conn.send_json(message)
        if isinstance(message, bytes):
            message = message.decode('utf-8')
        return await conn.send_text(message)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            await self.send_message(connection, message)
