"""add update and create time

Revision ID: aac5120dca8e
Revises: f2d6aba28d7d
Create Date: 2024-12-09 14:39:43.695129

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = 'aac5120dca8e'
down_revision = 'f2d6aba28d7d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subtodo', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('subtodo', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('todo', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('todo', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todo', 'updated_at')
    op.drop_column('todo', 'created_at')
    op.drop_column('subtodo', 'updated_at')
    op.drop_column('subtodo', 'created_at')
    # ### end Alembic commands ###