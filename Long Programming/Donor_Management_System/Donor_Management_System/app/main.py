from fastapi import FastAPI
from app.database import Base, engine
from app.donor_routes import router as donor_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(donor_router)