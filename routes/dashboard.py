from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")


router = APIRouter()

# @router.get('/device', tags=["device"])
# async def get_device_info():
#     return "hello all"

@router.get("/dashboard",tags=["Dashboard"], response_class= HTMLResponse())
async def get_dashboard(request:Request):
    content = {"request":request}
    return templates.TemplateResponse("dashboard.html", content)