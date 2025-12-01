from fastapi import FastAPI, Body

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "message": "FastAPI server is running"}

@app.post("/receive")
async def receive(body: str = Body(..., media_type="text/plain")):
    print("Received:", body)
    return {"received": body}
