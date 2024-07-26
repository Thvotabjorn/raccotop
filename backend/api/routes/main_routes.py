from fastapi import APIRouter, HTTPException, UploadFile
from api.routes.auth_routes import auth_router
from api.routes.api_routes import api_router

main_router = APIRouter()
main_router.include_router(auth_router, api_router)


@main_router.get("/hello_world/")
async def root():
    return {"message": "Hello World"}
