from fastapi import FastAPI
from routes import device,dashboard

app = FastAPI()

@app.get("/")
async def root():
    return {"API is Live" }

app.include_router(device.router)
app.include_router(dashboard.router)