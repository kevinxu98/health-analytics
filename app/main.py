from fastapi import FastAPI
from app.api.queries.user_queries import router as query_router
from app.api.commands.user_commands import router as command_router

app = FastAPI()

app.include_router(query_router, prefix="/query", tags=["Queries"])
app.include_router(command_router, prefix="/command", tags=["Commands"])