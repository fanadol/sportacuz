"""empty message

Revision ID: ae9cc5eab7d8
Revises: 294051df01de
Create Date: 2018-08-20 14:47:00.004867

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae9cc5eab7d8'
down_revision = '294051df01de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('athlete', sa.Column('jersey_number', sa.Integer(), nullable=True))
    op.drop_column('athlete', 'phone_number')
    op.create_unique_constraint(None, 'team', ['logo'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'team', type_='unique')
    op.add_column('athlete', sa.Column('phone_number', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
    op.drop_column('athlete', 'jersey_number')
    # ### end Alembic commands ###
