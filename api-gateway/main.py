from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from routers import layout_analysis, logo_redaction

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    layout_analysis.router,
    prefix="/layout-analysis",
    tags=["Layout Analysis"]
)

app.include_router(
    logo_redaction.router,
    prefix="/logo-redaction",
    tags=["Logo Redaction"]
)

@app.get("/results/{slug}", tags=["Get Results"])
def get_results(slug):
    # TODO: Add error handling
    return FileResponse(f"results/{slug}.png")