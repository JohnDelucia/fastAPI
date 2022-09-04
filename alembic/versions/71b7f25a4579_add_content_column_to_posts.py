"""add content column to posts

Revision ID: 71b7f25a4579
Revises: 41b4dcd172fb
Create Date: 2022-09-04 13:08:42.009760

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71b7f25a4579'
down_revision = '41b4dcd172fb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
