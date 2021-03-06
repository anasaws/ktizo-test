"""Added user table

Revision ID: 467056c3a913
Revises: 
Create Date: 2022-02-08 18:43:45.288266

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = '467056c3a913'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('full_name', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('spotify_artist_profile', sa.String(length=255), nullable=True),
    sa.Column('favourite_music_style', sa.String(length=255), nullable=True),
    sa.Column('favourite_music_mood', sa.String(length=255), nullable=True),
    sa.Column('yourown_music', sa.String(length=255), nullable=True),
    sa.Column('favourite_music_topic', sa.String(length=255), nullable=True),
    sa.Column('master', sa.String(length=255), nullable=True),
    sa.Column('publish_control', sa.String(length=255), nullable=True),
    sa.Column('outside_income', sa.String(length=255), nullable=True),
    sa.Column('established_artist', sa.String(length=255), nullable=True),
    sa.Column('company', sa.String(length=255), nullable=True),
    sa.Column('linkedin_profile', sa.String(length=255), nullable=True),
    sa.Column('project_seek_music', sa.String(length=255), nullable=True),
    sa.Column('turn_around_time', sa.String(length=255), nullable=True),
    sa.Column('project_budject', sa.String(length=255), nullable=True),
    sa.Column('syncs_seek', sa.String(length=255), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('full_name'),
    sa.UniqueConstraint('password')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
