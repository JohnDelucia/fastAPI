"""create posts table

Revision ID: 41b4dcd172fb
Revises: 
Create Date: 2022-09-04 13:00:26.310098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41b4dcd172fb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable = False, primary_key = True),
    sa.Column('title', sa.String(), nullable = False))
    pass

def downgrade() -> None:
    op.drop_table('posts')
    pass
