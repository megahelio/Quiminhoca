from fastapi import FastAPI
from api.routes import router as api_router

app = FastAPI(title="Chemical Formula Lookup API")

app.include_router(api_router)