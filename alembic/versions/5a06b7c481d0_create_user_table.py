"""create user table

Revision ID: 5a06b7c481d0
Revises: 
Create Date: 2021-11-28 18:51:11.301951

"""
from enum import unique
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import false


# revision identifiers, used by Alembic.
revision = '5a06b7c481d0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    conn.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')
    op.create_table(
        "users",
        sa.Column("id", 
            sa.dialects.postgresql.UUID(as_uuid=True),
            primary_key=True,
            nullable=False,
            server_default=sa.text('uuid_generate_v4()')
        ),
        sa.Column("first_name", sa.String(256), nullable=False),
        sa.Column("last_name", sa.String(256), nullable=False),
        sa.Column("email", sa.String(256), nullable=False, unique=True),
        sa.Column("password", sa.String(), nullable= False),
        sa.Column("created_at", sa.DateTime(False), nullable = False, default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(False)),
        sa.Column("deleted_at", sa.DateTime(False))
    )


def downgrade():
    op.drop_table("users")
