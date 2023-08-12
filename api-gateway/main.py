from fastapi import FastAPI
from fastapi.responses import FileResponse

from routers import layout_analysis, logo_redaction

app = FastAPI()

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