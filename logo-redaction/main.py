from typing_extensions import Annotated

from fastapi import FastAPI, File, UploadFile

from model.logo_redaction import redact_logo 

app = FastAPI()


@app.post("/")
async def redact_logo(file: Annotated[UploadFile, File(description="An image file")]):
    redact_logo(file.file)
    return {"filename": file.filename}