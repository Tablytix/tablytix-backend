import requests
from typing import Annotated

from fastapi import APIRouter, File, UploadFile

router = APIRouter()

@router.post("/")
async def main(file: Annotated[UploadFile, File(description="An image file")]):
    # TODO: Add error handling
    contents = await file.read()
    files = {"file": (file.filename, contents, file.content_type)}
    r = requests.post("http://layout-analysis/", files=files)
    return r.json()
