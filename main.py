from fastapi import FastAPI, Query
from datetime import datetime

app = FastAPI()

# In-memory "database" just for testing
stored_data: list[dict] = []


@app.get("/")
def root():
    return {"status": "ok", "message": "FastAPI server is running"}


# Example:
#   GET /receive?data=hello
@app.get("/receive")
async def receive(data: str = Query(..., description="Data to store on server")):
    item = {
        "data": data,
        "time": datetime.utcnow().isoformat() + "Z",
    }

    # "Put" data in the server (in-memory list)
    stored_data.append(item)

    # Log to console
    print("✅ Received:", item)
    print("📦 All stored data now:", stored_data)

    return {
        "status": "ok",
        "received": item,
        "total_items": len(stored_data),
    }


# Optional: see everything currently stored
@app.get("/all")
async def get_all():
    return stored_data
