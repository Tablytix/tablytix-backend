from typing import Annotated

from fastapi import FastAPI, File, UploadFile

from model.layout_analysis import layout_analysis

app = FastAPI()


@app.post("/")
async def upload(file: Annotated[UploadFile, File(description="An image file")]):
    filename = layout_analysis(file.file)
    return {"filename": filename}