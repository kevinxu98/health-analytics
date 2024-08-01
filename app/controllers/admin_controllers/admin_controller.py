from fastapi import APIRouter
from app.db.database import create_database, create_containers


router = APIRouter()

@router.get("/test_admin_endpoint")
def test_query_endpoint():
    return {"message": "success"}

@router.post("/generate_database")
def generate_database():
    try:
        create_database()
        return {"message": "database created successfully"}
    except Exception as e:
        return {"error": str(e)}

@router.post("/generate_containers")
def generate_containers():
    try:
        create_containers()
        return {"message": "containers created successfully"}
    except Exception as e:
        return {"error": str(e)}