from typing import Annotated

from fastapi import FastAPI, File, UploadFile
import pdfplumber


app = FastAPI()

def extract_table(file):
    pdf = pdfplumber.open(file)
    p0 = pdf.pages[0]
    return p0.extract_table()

@app.post("/")
async def table_extraction(file: Annotated[UploadFile, File(description="A pdf file")]):
    table = extract_table(file.file)
    return table