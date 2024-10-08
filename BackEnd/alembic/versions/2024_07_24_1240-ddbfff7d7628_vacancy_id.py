"""vacancy_id

Revision ID: ddbfff7d7628
Revises: d9a32f411328
Create Date: 2024-07-24 12:40:54.869535

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ddbfff7d7628"
down_revision: Union[str, None] = "d9a32f411328"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("temp_vacancies", sa.Column("vacancy_id", sa.String(), nullable=False))
    op.add_column("vacancy", sa.Column("vacancy_id", sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("vacancy", "vacancy_id")
    op.drop_column("temp_vacancies", "vacancy_id")
    # ### end Alembic commands ###
