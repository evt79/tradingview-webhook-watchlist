from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

signals = []

@app.post("/alert")
async def alert_endpoint(request: Request):
    body = await request.body()
    data = json.loads(body)
    signals.append(data)
    return {"status": "ok", "message": "Señal recibida"}

@app.get("/watchlist")
def get_watchlist():
    return signals