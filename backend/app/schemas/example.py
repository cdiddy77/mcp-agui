from typing import Any

from pydantic import BaseModel


class ExampleRequest(BaseModel):
    name: str
    description: str | None = None


class ExampleResponse(BaseModel):
    message: str
    data: dict[str, Any] | None = None
