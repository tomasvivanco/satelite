from fastapi import Header, HTTPException, status


async def verify_api_key(x_api_key: str | None = Header(default=None)) -> None:
    """Optional placeholder for production API key enforcement."""
    if x_api_key is None:
        return

    if len(x_api_key.strip()) < 12:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key.",
        )
