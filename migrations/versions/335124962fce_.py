"""empty message

Revision ID: 335124962fce
Revises: 28168a12f2c4
Create Date: 2018-02-18 08:47:56.294664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '335124962fce'
down_revision = '28168a12f2c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_test_api_number'), 'test', ['api_number'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_test_api_number'), table_name='test')
    # ### end Alembic commands ###
