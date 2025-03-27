from fastapi import FastAPI, Query, HTTPException, Body
import uvicorn
import os
from time import time
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse  # <-- Added HTMLResponse
from fastapi.staticfiles import StaticFiles
from SummaryOfText.pipeline.prediction import PredictionPipeline
from starlette.requests import Request

app = FastAPI()

templates = Jinja2Templates(directory="summary_api/templates")
app.mount("/static", StaticFiles(directory="summary_api/static"), name="static")

@app.get("/", response_class=HTMLResponse)  # Using HTMLResponse
async def index(request: Request):
    current_time = time()  # Get the current timestamp
    return templates.TemplateResponse("index.html", {"request": request, "time": current_time})

@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return {"message": "Training successfully Done!!"}
    except Exception as e:
        return {"message": f"Error occurred: {e}"}

@app.post("/predict")  # Changed to POST
async def predict_route(request: Request, body: dict = Body(...)):
    try:
        text = body.get('text')
        if not text:
            raise HTTPException(status_code=400, detail="Text parameter is missing")
        
        obj = PredictionPipeline()
        summarized_text = obj.predict(text)
        return JSONResponse(content={"summary": summarized_text})  # JSON Response for easy consumption by JS
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error during prediction: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
