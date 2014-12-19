"""Add username column

Revision ID: 194e5dd5e1d
Revises: 48ebc090cfde
Create Date: 2014-12-16 14:21:33.230655

"""

# revision identifiers, used by Alembic.
revision = '194e5dd5e1d'
down_revision = '48ebc090cfde'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'user',
        sa.Column('username', sa.String(length=255), nullable=True)
    )
    op.create_unique_constraint(None, 'user', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'username')
    # ### end Alembic commands ###
