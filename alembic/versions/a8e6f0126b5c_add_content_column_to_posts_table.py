"""add content column to posts table

Revision ID: a8e6f0126b5c
Revises: 2ff590975f92
Create Date: 2022-01-31 21:45:11.399409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8e6f0126b5c'
down_revision = '2ff590975f92'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
