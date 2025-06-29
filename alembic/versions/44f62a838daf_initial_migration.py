"""Initial migration

Revision ID: 44f62a838daf
Revises: 
Create Date: 2025-06-19 13:32:25.848974

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '44f62a838daf'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_dishes_name'), table_name='dishes')
    op.create_index(op.f('ix_dishes_name'), 'dishes', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_dishes_name'), table_name='dishes')
    op.create_index(op.f('ix_dishes_name'), 'dishes', ['name'], unique=True)
    # ### end Alembic commands ###
