"""empty message

Revision ID: 3085c287c339
Revises: 98e596147cc0
Create Date: 2024-10-03 13:56:35.447044

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3085c287c339'
down_revision = '98e596147cc0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_index('ix_post_user_id')
        batch_op.create_index(batch_op.f('ix_post_user_id'), ['user_id'], unique=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.String(length=256), nullable=True))
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_seen')
        batch_op.drop_column('about_me')

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_post_user_id'))
        batch_op.create_index('ix_post_user_id', ['user_id'], unique=1)

    # ### end Alembic commands ###
