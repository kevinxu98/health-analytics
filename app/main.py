from fastapi import FastAPI
import uvicorn
from app.controllers.query_controllers.query_controlller import router as query_controllers
from app.controllers.command_controllers.command_controller import router as command_controllers

app = FastAPI(title="Healthcare Analytics Microservice", version="0.0.1")

app.include_router(query_controllers, prefix="/query", tags=["Queries"])
app.include_router(command_controllers, prefix="/command", tags=["Commands"])

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)