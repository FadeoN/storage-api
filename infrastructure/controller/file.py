import os
import sys

import aiofiles
from fastapi import APIRouter, UploadFile, File
from starlette import status
from starlette.responses import FileResponse

from infrastructure.configuration.app import APP_OPTIONS

router = APIRouter()


@router.get("/{filename}")
async def get_file(filename):
    return FileResponse(os.path.join(APP_OPTIONS.storage_options.save_location, filename))


@router.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(APP_OPTIONS.storage_options.save_location, file.filename)  # TODO: Assign unique id
    async with aiofiles.open(file_location, "wb") as out_file:
        content = await file.read(APP_OPTIONS.storage_options.read_chunk_size)
        while content:
            await out_file.write(content)
            content = await file.read(APP_OPTIONS.storage_options.read_chunk_size)
    return {"filename": file.filename}
