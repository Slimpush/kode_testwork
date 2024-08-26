from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()

users: dict[str, str] = {"user1": "Pwtest1", "user2": "Pwtest2"}


def get_current_user(credentials: HTTPBasicCredentials = Depends(security)) -> str:
    if users.get(credentials.username) == credentials.password:
        return credentials.username
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Пользователь не авторизован",
    )
