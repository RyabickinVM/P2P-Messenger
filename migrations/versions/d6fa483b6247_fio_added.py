"""FIO added

Revision ID: d6fa483b6247
Revises: 64b4815c94c6
Create Date: 2024-01-18 21:47:40.571839

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd6fa483b6247'
down_revision: Union[str, None] = '64b4815c94c6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('last_name', sa.String(length=20), nullable=True))
    op.add_column('user', sa.Column('first_name', sa.String(length=20), nullable=True))
    op.add_column('user', sa.Column('surname', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'surname')
    op.drop_column('user', 'first_name')
    op.drop_column('user', 'last_name')
    # ### end Alembic commands ###