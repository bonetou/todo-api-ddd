from fastapi import APIRouter

health_router = APIRouter(tags=["health"])

@health_router.get("/_health")
async def health():
    return {"status": "ok"}
