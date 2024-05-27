"""ProductSchema

Revision ID: 81698aa95fa2
Revises: 4b7050c617c3
Create Date: 2024-05-27 10:27:18.303886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81698aa95fa2'
down_revision = '4b7050c617c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('taxable', sa.Boolean(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Product_id'), 'Product', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Product_id'), table_name='Product')
    op.drop_table('Product')
    # ### end Alembic commands ###