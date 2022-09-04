"""add foreign key to post table

Revision ID: c44805f1f01d
Revises: 579395ff2aab
Create Date: 2022-09-04 13:23:12.456389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c44805f1f01d'
down_revision = '579395ff2aab'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable = False))
    op.create_foreign_key('post_users_fk', source_table = "posts", referent_table = "users",
    local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constaint('post_users_fk', table_name = "posts")
    op.drop_column('posts', 'owner_id')
    pass
