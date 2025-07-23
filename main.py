from fastapi import FastAPI
import os
from dotenv import load_dotenv
from routers import auth, memory, logs, commands

app = FastAPI(title="NEXI Backend API", version="0.1.0")

load_dotenv()
@app.get("/") 
async def root():
    return {"message": f"Server running on port: {os.getenv('PORT')}"} 

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(memory.router, prefix="/memory", tags=["Memory"])
app.include_router(logs.router, prefix="/logs", tags=["Logs"])
app.include_router(commands.router, prefix="/commands", tags=["Commands"]) 