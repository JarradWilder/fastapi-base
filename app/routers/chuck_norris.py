from fastapi import APIRouter
from services.chuck_norris_service import chuck_norris_service

router = APIRouter()

@router.get("/chuck-norris/random")
async def get_random_chuck_norris_joke():
    joke = await chuck_norris_service.get_random_joke()
    return joke