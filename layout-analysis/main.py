from typing import Annotated

from fastapi import FastAPI, File, UploadFile

from model.layout_analysis import analyze_layout 

app = FastAPI()


@app.post("/")
async def layout_analysis(file: Annotated[UploadFile, File(description="An image file")]):
    filename = analyze_layout(file.file)
    return {"filename": filename}