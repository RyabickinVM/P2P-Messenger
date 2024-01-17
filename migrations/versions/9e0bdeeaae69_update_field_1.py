"""Update field (1)

Revision ID: 9e0bdeeaae69
Revises: 4300f5880642
Create Date: 2024-01-17 21:26:36.464853

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9e0bdeeaae69'
down_revision: Union[str, None] = '4300f5880642'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('room_user', 'is_owner',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('room_user', 'is_owner',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###
