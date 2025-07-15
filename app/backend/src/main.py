from contextlib import asynccontextmanager
from fastapi import FastAPI
import sqlalchemy
from sqlmodel import SQLModel
from routers.lookup import lookupRouter
from fastapi.middleware.cors import CORSMiddleware
from routers.auth import authRouter
from db.database import engine
from config import get_logger

logger = get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    try:
        with engine.connect() as conn:
            conn.execute(sqlalchemy.text("SELECT 1"))
            logger.info("Conectado a la BD.")
    except sqlalchemy.exc.SQLAlchemyError as e:
        logger.error("Error al conectar con la BD:", e)
        raise e

    SQLModel.metadata.create_all(engine)

    yield  
    
    logger.info("Aplicación cerrándose...")
    
app = FastAPI(title="Quiminhoca", lifespan=lifespan)

app.include_router(lookupRouter)
app.include_router(authRouter)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # o tu dominio frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)