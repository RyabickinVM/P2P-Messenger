import logging
from typing import List

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from auth.schemas import UserRead
from aws.service import *
from models.models import *
from user.schemas import UserReadRequest, UserBaseReadRequest

logger = logging.getLogger(__name__)


async def get_user_by_id(session: AsyncSession, user_id: int) -> UserReadRequest:
    user_instance = (await session.execute(select(user).filter_by(id=user_id))).one()
    await session.commit()
    return UserReadRequest(
        user_id=user_instance.id,
        username=user_instance.username,
        email=user_instance.email,
        profile_pic_img_src=user_instance.image_url
    )


async def get_users_in_room(session: AsyncSession, room_id: int) -> List[UserReadRequest]:
    result = await session.execute(
        select(user)
        .join(room_user, user.c.id == room_user.c.user)
        .where(room_user.c.room == room_id)
    )
    rows = result.fetchall()
    users: List[UserReadRequest] = list()
    for row in rows:
        users.append(UserReadRequest(
            user_id=row[0],
            username=row[1],
            email=row[2],
            profile_pic_img_src=row[4]
        ))
    await session.commit()
    return users


async def get_user_image_url(current_user: UserRead) -> Optional[str]:
    return current_user.image_url


async def update_user(session: AsyncSession, current_user: UserRead, file: Optional[UploadFile]) -> Optional[
    UserBaseReadRequest]:
    try:
        file_to_name = await upload(file)
        image_url = await get_url(file_to_name.file_name)
        await session.execute(
            update(user)
            .where(user.c.id == current_user.id)
            .values(image_url=image_url))
        await session.commit()
        return UserBaseReadRequest(user_id=current_user.id, username=current_user.username,
                                   image_url=current_user.image_url)
    except Exception as e:
        logger.error(f"Error updating user: {e}")
        await session.rollback()
        return None
