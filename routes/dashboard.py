from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")


router = APIRouter()

@router.get("/dashboard",tags=["Dashboard"], response_class= HTMLResponse())
async def get_dashboard(request:Request):
    content = {"request":request}
    return templates.TemplateResponse("test.html", content) # dashboard.html