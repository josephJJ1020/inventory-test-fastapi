from fastapi import HTTPException, status

DBException = HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},)