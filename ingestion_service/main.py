from fastapi import FastAPI
import asyncio
import websockets
import json

app = FastAPI()

BINANCE_WS = "wss://stream.binance.com:9443/ws/btcusdt@trade"

@app.get("/health")
def health():
    return {"status": "ok"}

async def stream_binance():
    async with websockets.connect(BINANCE_WS) as ws:
        while True:
            msg = await ws.recv()
            data = json.loads(msg)
            print("[RAW]", data)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(stream_binance())
