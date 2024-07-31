from fastapi import APIRouter
from app.db.database import inialize_storage


router = APIRouter()

@router.get("/test_admin_endpoint")
def test_query_endpoint():
    return {"message": "success"}

@router.post("/create_database")
def create_database():
    try:
        inialize_storage()
        return {"message": "database created successfully"}
    except Exception as e:
        return {"error": str(e)}

