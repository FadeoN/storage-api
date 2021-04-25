from fastapi import APIRouter

from infrastructure.controller.file import router as pose_estimation_router

api_router = APIRouter()

api_router.include_router(pose_estimation_router, prefix="/files", tags=["files"])
