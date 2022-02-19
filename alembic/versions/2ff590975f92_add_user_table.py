"""add user table

Revision ID: 2ff590975f92
Revises: 2c668c05d822
Create Date: 2022-01-31 21:39:26.561380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ff590975f92'
down_revision = '2c668c05d822'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                sa.Column('id', sa.Integer(), nullable=False),
                sa.Column('email', sa.String(), nullable=False),
                sa.Column('password', sa.String(), nullable=False),
                sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                            server_default=sa.text('now()'), nullable=False),
                sa.PrimaryKeyConstraint('id'),
                sa.UniqueConstraint('email')
                )
    pass


def downgrade():
    op.drop_table('users')
    pass
