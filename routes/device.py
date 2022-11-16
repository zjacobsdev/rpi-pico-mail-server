from fastapi import APIRouter
from schemas import DeviceResponseBase

router = APIRouter()

@router.get('/device', tags=["Device"],response_model=DeviceResponseBase, deprecated=True)
async def get_device_info():
    return "Device Infromation"


@router.get("/device-status", tags = ["Device"],response_model=DeviceResponseBase, deprecated=True) 
async def get_device_status():
    """
    - Check the awake status of the device every five minutes
     - checks if device is on and working normally 
    """
    return {"message": "Device Status"}
