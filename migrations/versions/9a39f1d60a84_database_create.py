"""Database create

Revision ID: 9a39f1d60a84
Revises: 
Create Date: 2023-10-11 15:08:14.090381

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9a39f1d60a84'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('room',
    sa.Column('room_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('room_name', sa.String(length=40), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('creation_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('room_id'),
    sa.UniqueConstraint('room_name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.Column('creation_date', sa.DateTime(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('message',
    sa.Column('message_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('message_data', sa.String(length=4096), nullable=False),
    sa.Column('media_file_url', sa.String(), nullable=True),
    sa.Column('creation_date', sa.DateTime(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('room', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['room'], ['room.room_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('message_id')
    )
    op.create_index('idx_message__room', 'message', ['room'], unique=False)
    op.create_index('idx_message__user', 'message', ['user'], unique=False)
    op.create_table('room_user',
    sa.Column('creation_date', sa.DateTime(), nullable=False),
    sa.Column('is_chosen', sa.Boolean(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('room', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['room'], ['room.room_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user'], ['user.id'], ondelete='CASCADE')
    )
    op.create_index('idx_chosen__room', 'room_user', ['room'], unique=False)
    op.create_index('idx_chosen__user', 'room_user', ['user'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_chosen__user', table_name='room_user')
    op.drop_index('idx_chosen__room', table_name='room_user')
    op.drop_table('room_user')
    op.drop_index('idx_message__user', table_name='message')
    op.drop_index('idx_message__room', table_name='message')
    op.drop_table('message')
    op.drop_table('user')
    op.drop_table('room')
    # ### end Alembic commands ###
