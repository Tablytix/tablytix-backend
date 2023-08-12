from typing import Annotated

from fastapi import FastAPI, File, UploadFile

from model.layout_analysis import analyze_layout 

app = FastAPI()


@app.post("/")
async def layout_analysis(file: Annotated[UploadFile, File(description="An image file")]):
    slug = analyze_layout(file.file)
    return {"slug": slug}