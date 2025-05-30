"""Fixed foreign key issues

Revision ID: ff294fc496de
Revises: 
Create Date: 2025-04-23 22:40:12.243338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff294fc496de'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('avatar_url', sa.String(length=256), nullable=True),
    sa.Column('public_repos', sa.Integer(), nullable=True),
    sa.Column('followers', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('repositories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('stars', sa.Integer(), nullable=True),
    sa.Column('forks', sa.Integer(), nullable=True),
    sa.Column('language', sa.String(length=64), nullable=True),
    sa.Column('url', sa.String(length=256), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('repositories')
    op.drop_table('user')
    # ### end Alembic commands ###
