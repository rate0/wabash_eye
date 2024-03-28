import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGODB_HOST: str = os.getenv("MONGO_HOST")
    MONGO_PORT: int = int(os.getenv("MONGO_PORT"))
    MONGO_DBNAME: str = os.getenv("MONGO_DBNAME")
    MONGO_COLLECTION: str = os.getenv("MONGO_COLLECTION")
