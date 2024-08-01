from fastapi import APIRouter
from app.queries.queries import GetProfileQuery
router = APIRouter()

@router.get("/test_query_endpoint")
def test_query_endpoint():
    return {"message": "Hello from test_query_endpoint!"}

