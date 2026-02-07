from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="School Timetable Engine")

app.include_router(router)
