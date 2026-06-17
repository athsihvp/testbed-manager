from fastapi import APIRouter
from services.image_service import get_images

router = APIRouter()

@router.get("/images")
def images():
    return {"images": get_images()}