"""empty message

Revision ID: 6dec45ef2f87
Revises: 12e6489d20bc
Create Date: 2021-07-25 23:46:29.800102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6dec45ef2f87'
down_revision = '12e6489d20bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('app_tags', 'created_at')
    op.drop_column('app_tags', 'updated_at')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('app_tags', sa.Column('updated_at', sa.DATE(), autoincrement=False, nullable=True))
    op.add_column('app_tags', sa.Column('created_at', sa.DATE(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
