# run this script to create all database tables
import asyncio
from core.database import engine
from models import Base

async def init_database():
    """Initialize the database with all tables."""
    print("Creating database tables...")
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    print("Database tables created successfully!")
    print("Tables created:")
    print("- users")
    print("- nexi_devices") 
    print("- logs")

if __name__ == "__main__":
    asyncio.run(init_database()) 