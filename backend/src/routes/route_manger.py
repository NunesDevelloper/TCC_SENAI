from fastapi import APIRouter
from fastapi.responses import RedirectResponse


mr = APIRouter()

@mr.get("/", include_in_schema=False)
async def root_to_docs() -> RedirectResponse:
    return RedirectResponse("/docs")
