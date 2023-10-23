from typing import Optional, List

from pydantic import BaseModel, Field

from message.schemas import MessageRead
from user.schemas import UserReadRequest


class RoomBaseRequest(BaseModel):
    room_name: str


class RoomCreateRequest(RoomBaseRequest):
    pass


class RoomBaseInfoRequest(RoomBaseRequest):
    room_id: int


class RoomBaseInfoForUserRequest(RoomBaseInfoRequest):
    is_favorites: bool


class RoomReadRequest(RoomBaseInfoRequest):
    members: List[UserReadRequest] = Field(...)
    messages: Optional[List[MessageRead]] = Field(...)


class FavoriteRequest(BaseModel):
    room_id: int
    is_chosen: bool
