from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from routers import images, provision

app = FastAPI(title="Testbed Manager MVP")

# routers
app.include_router(images.router, prefix="/api")
app.include_router(provision.router, prefix="/api")

# static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# templates
templates = Jinja2Templates(directory="templates")


@app.get("/")
def root():
    return {"status": "Testbed Manager running"}


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse(
        request,
        "dashboard.html",
        {"request": request}
    )