from fastapi import APIRouter

router = APIRouter()

@router.get("/_health")
async def health():
    return {"status": "ok"}
