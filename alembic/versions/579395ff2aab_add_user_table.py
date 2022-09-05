"""add user table

Revision ID: 579395ff2aab
Revises: 71b7f25a4579
Create Date: 2022-09-04 13:13:03.226021

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '579395ff2aab'
down_revision = '71b7f25a4579'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
