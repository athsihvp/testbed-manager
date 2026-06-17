from fastapi import APIRouter
from pydantic import BaseModel
from services.provisioning_service import create_playbook

router = APIRouter()


class ProvisionRequest(BaseModel):
    image: str
    blades: list


@router.post("/provision")
def provision(req: ProvisionRequest):

    file_path = create_playbook(req.image, req.blades)

    return {
        "status": "success",
        "playbook": file_path
    }