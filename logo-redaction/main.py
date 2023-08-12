from typing_extensions import Annotated

from fastapi import FastAPI, File, UploadFile

from model.logo_redaction import redact_logo 

app = FastAPI()


@app.post("/")
def logo_redaction(file: Annotated[UploadFile, File(description="An image file")]):
    slug = redact_logo(file.file)
    return {"slug": slug}