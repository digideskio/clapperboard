"""Initial db structure

Revision ID: 461fe3224e3f
Revises: None
Create Date: 2014-11-28 17:49:16.822507

"""

# revision identifiers, used by Alembic.
revision = '461fe3224e3f'
down_revision = None

from alembic import op
import sqlalchemy as sa



def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('technology',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movie',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('url_code', sa.String(length=255), nullable=True),
    sa.Column('show_start', sa.Date(), nullable=True),
    sa.Column('show_end', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('theatre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('en_name', sa.String(length=255), nullable=True),
    sa.Column('url_code', sa.String(length=255), nullable=True),
    sa.Column('st_url_code', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('imdb_data',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('genre', sa.String(length=255), nullable=True),
    sa.Column('country', sa.String(length=255), nullable=True),
    sa.Column('director', sa.String(length=255), nullable=True),
    sa.Column('cast', sa.String(length=4096), nullable=True),
    sa.Column('runtime', sa.Integer(), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('show_time',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('theatre_id', sa.Integer(), nullable=True),
    sa.Column('hall_id', sa.Integer(), nullable=True),
    sa.Column('technology_id', sa.Integer(), nullable=True),
    sa.Column('date_time', sa.DateTime(), nullable=True),
    sa.Column('order_url', sa.String(length=255), nullable=True),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.ForeignKeyConstraint(['technology_id'], ['technology.id'], ),
    sa.ForeignKeyConstraint(['theatre_id'], ['theatre.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('last_fetched',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_time', sa.DateTime(), nullable=True),
    sa.Column('theatre_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['theatre_id'], ['theatre.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('last_fetched')
    op.drop_table('show_time')
    op.drop_table('imdb_data')
    op.drop_table('theatre')
    op.drop_table('movie')
    op.drop_table('technology')
    ### end Alembic commands ###
