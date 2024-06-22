from fastapi import APIRouter

router = APIRouter()

@router.get("/test_command_endpoint")
def test_command_endpoint():
    return {"message": "Hello from test_command_endpoint!"}