"""empty message

Revision ID: 344fc2873a90
Revises: 
Create Date: 2020-03-15 03:35:26.207682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '344fc2873a90'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=80), nullable=True),
    sa.Column('lastname', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('location', sa.String(length=120), nullable=True),
    sa.Column('biography', sa.String(length=255), nullable=True),
    sa.Column('date_joined', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profile')
    # ### end Alembic commands ###
