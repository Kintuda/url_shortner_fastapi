"""create oauth token table

Revision ID: 02858a5be83f
Revises: 5a06b7c481d0
Create Date: 2021-11-28 18:51:24.894299

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql.base import UUID


# revision identifiers, used by Alembic.
revision = '02858a5be83f'
down_revision = '5a06b7c481d0'
branch_labels = None
depends_on = None


def upgrade():
       op.create_table(
        "oauth_tokens",
        sa.Column("id", 
            sa.dialects.postgresql.UUID(as_uuid=True),
            primary_key=True,
            nullable=False,
            server_default=sa.text('uuid_generate_v4()')
        ),
        sa.Column("access_token", sa.String(), nullable=False),
        sa.Column("expires_at", sa.DateTime(False), nullable=False),
        sa.Column('user_id', UUID, nullable=False),
        sa.Column("created_at", sa.DateTime(False), default=sa.func.now()),
        sa.ForeignKeyConstraint(('user_id',), ['users.id']),
    )



def downgrade():
    op.drop_table("oauth_tokens")
