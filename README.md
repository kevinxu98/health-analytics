# Healthcare Analytics Microservice

## Description

Project demonstrates how to implement a microservice using the CQRS pattern and event-sourcing. Application simulates a healthcare analytics system allow users to append reports into system and query the reports. Eech "event" is a new revision of the report and is stored in a event store, while the latest version of the report is simultaneously stored in a read model for quick access. This separation of concerns allows for a scalable and flexible system.

Please see app_architecture.png in this directory for a visual representation of the system.

Technologies:
- Python
- FastAPI
- OPENAPI/Swagger Docs
- CQRS
- Event-Sourcing
- CosmosDB
- Azure
- Git
- Github