from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    image_url: Optional[str]


class UserBaseReadRequest(UserBase):
    user_id: int


class UserReadRequest(UserBaseReadRequest):
    email: str


class UserPersonalReadRequest(UserBaseReadRequest):
    last_name: Optional[str]
    first_name: Optional[str]
    surname: Optional[str]


class UserImageUploadRequest(BaseModel):
    image_url: str


class UserUpdateRequest(BaseModel):
    password: Optional[str] = None
    username: Optional[str] = None
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    surname: Optional[str] = None
