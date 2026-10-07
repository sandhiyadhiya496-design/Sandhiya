from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

# Project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Templates folder
templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)

# Static folder
app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static"
)


# Home page
@app.get("/")
def home():
    return FileResponse(
        str(BASE_DIR / "templates" / "index.html")
    )


# Result page
@app.post("/result", response_class=HTMLResponse)
def result(
    request: Request,
    name: str = Form(...),
    age: int = Form(...),
    height: float = Form(...),
    weight: float = Form(...),
    goal: str = Form(...)
):

    data = {
        "request": request,
        "name": name,
        "age": age,
        "height": height,
        "weight": weight,
        "goal": goal
    }

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context=data
    )