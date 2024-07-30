from fastapi import FastAPI
from app.controllers.queries.user_queries import router as query_router
from app.controllers.commands.user_commands import router as command_router

app = FastAPI(title="Healthcare Analytics Microservice", version="0.0.1")

app.include_router(query_router, prefix="/query", tags=["Queries"])
app.include_router(command_router, prefix="/command", tags=["Commands"])