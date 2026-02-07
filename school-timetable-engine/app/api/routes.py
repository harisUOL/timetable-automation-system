from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {
        "message": "School Timetable Engine is running",
        "status": "OK"
    }

@router.post("/generate-timetable")
def generate_timetable():
    return {"status": "not implemented yet"}
