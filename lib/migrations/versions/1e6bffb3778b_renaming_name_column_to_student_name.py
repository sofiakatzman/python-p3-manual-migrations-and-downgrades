"""renaming name column to student_name

Revision ID: 1e6bffb3778b
Revises: a9c260d3011a
Create Date: 2023-05-31 21:26:13.065453

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e6bffb3778b'
down_revision = 'a9c260d3011a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'name', new_column_name='student_name')


def downgrade() -> None:
    op.alter_column('students', 'student_name', new_column_name='name')
