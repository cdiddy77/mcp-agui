from datetime import UTC, datetime, timedelta
from typing import Any


def create_access_token(
    subject: str | Any, expires_delta: timedelta | None = None
) -> str:
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(minutes=15)

    to_encode = {"exp": expire, "sub": str(subject)}
    return to_encode
