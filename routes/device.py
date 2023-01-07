from fastapi import APIRouter
from schemas import DeviceResponseBase

router = APIRouter()

@router.get('/device', tags=["Device"],response_model=DeviceResponseBase, deprecated=True)
async def get_device_info():
    try:
        #potential securityfeature
        # if(!device_name)
        #     return {"message": "Device Infomation"}
      return {"message": "Device Infomation"}
    except:
        return {"message":"Device not Available"}


@router.get("/device-status", tags = ["Device"],response_model=DeviceResponseBase, deprecated=True) 
async def get_device_status():
    """
    - Check the awake status of the device every five minutes
     - checks if device is on and working normally 
    """
    try:
        return {"message": "Device Status"}
    except: 
        return {"message":"Device not Available"}
