from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from lohany.fakan_kevitra import Mpamantatra

fampiharana = FastAPI()
fampiharana.mount("/static", StaticFiles(directory="endrika/static"), name="static")
endrika = Jinja2Templates(directory="endrika/takelaka")

boty = Mpamantatra()

@fampiharana.get("/", response_class=HTMLResponse)
async def fandraisana(request: Request):
    return endrika.TemplateResponse("fandraisana_mod.html", {"request": request})

@fampiharana.post("/manontany")
async def manontany(request: Request):
    tahiry = await request.json()
    fanontaniana = tahiry.get("fanontaniana")
    valiny = boty.valio(fanontaniana)
    return {"valiny": valiny}