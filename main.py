from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "message": "FastAPI server is running"}

@app.post("/receive")
async def receive(data: dict):
    print("Received data:", data)  # 👈 this will appear in Render logs
    return {"received": data}
