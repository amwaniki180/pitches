"""Update models

Revision ID: 3a574c624d05
Revises: 16f4f0086983
Create Date: 2019-07-03 09:27:42.976500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a574c624d05'
down_revision = '16f4f0086983'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('date', sa.String(), nullable=True),
    sa.Column('time', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('pitches', sa.Column('bio', sa.String(), nullable=True))
    op.add_column('pitches', sa.Column('email', sa.String(), nullable=True))
    op.add_column('pitches', sa.Column('name', sa.String(), nullable=True))
    op.add_column('pitches', sa.Column('profile_pic', sa.String(), nullable=True))
    op.drop_column('pitches', 'category')
    op.drop_column('pitches', 'title')
    op.drop_column('pitches', 'content')
    op.drop_column('pitches', 'date')
    op.add_column('users', sa.Column('name', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('password_hash', sa.String(length=255), nullable=True))
    op.create_index(op.f('ix_users_name'), 'users', ['name'], unique=False)
    op.drop_index('ix_users_username', table_name='users')
    op.drop_column('users', 'username')
    op.drop_column('users', 'password_secure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('username', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.create_index('ix_users_username', 'users', ['username'], unique=False)
    op.drop_index(op.f('ix_users_name'), table_name='users')
    op.drop_column('users', 'password_hash')
    op.drop_column('users', 'name')
    op.add_column('pitches', sa.Column('date', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('pitches', sa.Column('content', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('pitches', sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('pitches', sa.Column('category', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('pitches', 'profile_pic')
    op.drop_column('pitches', 'name')
    op.drop_column('pitches', 'email')
    op.drop_column('pitches', 'bio')
    op.drop_table('comments')
    # ### end Alembic commands ###
