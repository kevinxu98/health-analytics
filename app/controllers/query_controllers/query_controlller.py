from fastapi import APIRouter, Query
from app.db.projection_store import ProjectionStore
from app.handlers.query_handlers.query_handlers import GetProfileQueryHandler
from app.queries.queries import GetProfileQuery
router = APIRouter()

@router.get("/test_query_endpoint")
def test_query_endpoint():
    return {"message": "Hello from test_query_endpoint!"}

@router.get("/get_profile")
async def get_profile(tenant_id: str = Query(...), id: str = Query(...)):
    try:
        return await GetProfileQueryHandler(ProjectionStore()).handle(
            GetProfileQuery(
                tenant_id=tenant_id,
                id=id
                )
            )
    except Exception as e:
        return {"error": str(e)}
