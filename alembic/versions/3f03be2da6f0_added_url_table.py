"""Added url table

Revision ID: 3f03be2da6f0
Revises: 02858a5be83f
Create Date: 2021-12-14 23:29:37.734573

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql.base import UUID

# revision identifiers, used by Alembic.
revision = '3f03be2da6f0'
down_revision = '02858a5be83f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "urls",
        sa.Column("id",
                  sa.String(22),
                  primary_key=True,
                  nullable=False
                  ),
        sa.Column("original_url", sa.String(), nullable=False),
        sa.Column('user_id', UUID, nullable=False),
        sa.Column("created_at", sa.DateTime(False), default=sa.func.now()),
        sa.Column("deleted_at", sa.DateTime(False)),
        sa.ForeignKeyConstraint(('user_id',), ['users.id']),
    )


def downgrade():
    op.drop_table("urls")
