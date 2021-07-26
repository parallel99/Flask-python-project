"""empty message

Revision ID: 59baf40b0103
Revises: 2118239751d1
Create Date: 2021-07-26 17:40:01.943576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59baf40b0103'
down_revision = '2118239751d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('app_categories',
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('category_id')
    )
    op.create_table('app_question_categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('added_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['app_categories.category_id'], ),
    sa.ForeignKeyConstraint(['question_id'], ['app_questions.question_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('item')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=30), autoincrement=False, nullable=False),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('barcode', sa.VARCHAR(length=12), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(length=1024), autoincrement=False, nullable=False),
    sa.Column('owner', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['owner'], ['app_users.user_id'], name='item_owner_fkey'),
    sa.PrimaryKeyConstraint('id', name='item_pkey'),
    sa.UniqueConstraint('barcode', name='item_barcode_key'),
    sa.UniqueConstraint('description', name='item_description_key'),
    sa.UniqueConstraint('name', name='item_name_key')
    )
    op.drop_table('app_question_categories')
    op.drop_table('app_categories')
    # ### end Alembic commands ###