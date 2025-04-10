"""adding soft deletes and adding created at

Revision ID: 2f5c22dd2323
Revises: 4065c0114041
Create Date: 2025-04-09 15:58:55.209288

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2f5c22dd2323'
down_revision: Union[str, None] = '4065c0114041'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('deleted_at', sa.DateTime(), nullable=True))
    op.add_column('task', sa.Column('created_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'created_at')
    op.drop_column('task', 'deleted_at')
    # ### end Alembic commands ###
