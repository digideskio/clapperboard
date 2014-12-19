"""Add users table

Revision ID: 48ebc090cfde
Revises: 2e13bb9abcee
Create Date: 2014-12-16 11:06:37.974542

"""

# revision identifiers, used by Alembic.
revision = '48ebc090cfde'
down_revision = '2e13bb9abcee'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=True),
        sa.Column('password', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
