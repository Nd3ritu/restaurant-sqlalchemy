"""defined the relationship between the tables

Revision ID: 4540ea368dbc
Revises: a4c8fab4ebff
Create Date: 2023-12-15 12:00:19.124622

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4540ea368dbc'
down_revision: Union[str, None] = 'a4c8fab4ebff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
