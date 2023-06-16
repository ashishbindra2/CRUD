
from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

# Notice that you have to pass the request as part of the key-value pairs in the context for Jinja2.
# So, you also have to declare it in your path operation.
# By declaring response_class=HTMLResponse the docs UI will be able to know that the response will be HTML.

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})

# TODO find when to use asyn and when not

@app.get("/", response_class=HTMLResponse)
async def read_items(request:Request):
     return templates.TemplateResponse("index.html", {"request": request})

@app.post("/item/add", response_class=HTMLResponse)
async def add_item(request:Request):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})

@app.put('item/update',response_class=HTMLResponse)
async def update_item(request:Request):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})


@app.get("/items/{id}", response_class=HTMLResponse)
async def delete_item(request:Request):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})