"""Renaming students to scholars

Revision ID: a9c260d3011a
Revises: 791279dd0760
Create Date: 2023-05-31 21:21:25.062917

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9c260d3011a'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
