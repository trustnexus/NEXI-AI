from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from routers import auth, memory, logs, commands, upload, status
from core.database import engine
from models import Base
from config import settings

app = FastAPI(
    title="NEXI Backend API", 
    version="0.1.0",
    description="NEXI IoT Device Management Backend API"
)

# Load environment variables
load_dotenv()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    """Initialize database tables on startup."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("shutdown")
async def shutdown():
    """Clean up resources on shutdown."""
    await engine.dispose()

@app.get("/") 
async def root():
    return {
        "message": f"NEXI Backend API running on port: {settings.PORT}",
        "version": "0.1.0",
        "docs": "/docs"
    }

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(memory.router, prefix="/memory", tags=["Memory"])
app.include_router(logs.router, prefix="/logs", tags=["Logs"])
app.include_router(commands.router, prefix="/commands", tags=["Commands"])
app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(status.router, prefix="/status", tags=["Status"]) 