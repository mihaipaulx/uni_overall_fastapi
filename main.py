from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from script import get_overall

app = FastAPI()

app.mount("/static", StaticFiles(directory="./static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
  return templates.TemplateResponse(request=request, name="index.html")

@app.post("/get_overall")
async def process(request: Request):
  uni_url = await request.json()
  return StreamingResponse(get_overall(uni_url=uni_url))