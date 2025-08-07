from fastapi import APIRouter, HTTPException

from app.schemas.example import ExampleRequest, ExampleResponse

router = APIRouter()


@router.get("/", response_model=ExampleResponse)
async def get_example():
    return ExampleResponse(
        message="Hello from FastAPI!",
        data={"example": "data"},
    )


@router.post("/", response_model=ExampleResponse)
async def create_example(request: ExampleRequest):
    if not request.name:
        raise HTTPException(status_code=400, detail="Name is required")

    return ExampleResponse(
        message=f"Hello, {request.name}!",
        data={"name": request.name, "description": request.description},
    )
