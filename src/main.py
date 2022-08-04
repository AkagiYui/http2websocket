from fastapi import FastAPI
from starlette.exceptions import HTTPException
from fastapi.responses import Response
from fastapi import Request, WebSocket, WebSocketDisconnect

from websocket_manager import WebsocketManager

app = FastAPI()
ws_manager = WebsocketManager()


@app.websocket('/')
async def client_websocket(ws: WebSocket):
    await ws_manager.connect(ws)
    client = ws.client
    try:
        while True:
            s = await ws.receive_text()
            print(f'{client.host}:{client.port} < {s[:200]}')
    except WebSocketDisconnect:
        pass
    except Exception as e:
        print(f'{client.host}:{client.port} : {e}')
    ws_manager.disconnect(ws)


@app.exception_handler(HTTPException)
async def err(request: Request, _: HTTPException):
    try:
        content = await request.json()
    except Exception:
        content = await request.body()
        content = content.decode('utf-8')
    await ws_manager.broadcast({
        'path': request.url.path,
        'method': request.method,
        'headers': dict(request.headers),
        'content': content,
    })
    return Response(status_code=200)
