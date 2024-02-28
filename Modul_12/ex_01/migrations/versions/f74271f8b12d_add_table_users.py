"""add table users

Revision ID: f74271f8b12d
Revises: 9da1fe66da90
Create Date: 2024-02-28 17:22:05.533124

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f74271f8b12d'
down_revision: Union[str, None] = '9da1fe66da90'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('avatar', sa.String(length=250), nullable=True),
    sa.Column('refresh_token', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.add_column('todos', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('todos', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('todos', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'todos', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todos', type_='foreignkey')
    op.drop_column('todos', 'user_id')
    op.drop_column('todos', 'updated_at')
    op.drop_column('todos', 'created_at')
    op.drop_table('users')
    # ### end Alembic commands ###