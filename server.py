from fastapi import FastAPI, Request
from fastapi import FastAPI
from routes import device,dashboard
from schemas import DeviceResponseBase
from services.alerts  import pushDeviceAlert


app = FastAPI()

@app.get("/")
async def root():
    return {"API is Live" }

#Testing device notifications
@app.post("/send_notification", response_model= DeviceResponseBase)
async def send_mailbox_status_notification(request:Request):
    request = await request.json()
    response =  pushDeviceAlert(request)
    if not response:
         return{ "message":"Problem with push notification"}
    return {"message": response}

app.include_router(device.router)
app.include_router(dashboard.router)