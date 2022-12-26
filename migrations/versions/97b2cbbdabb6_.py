"""empty message

Revision ID: 97b2cbbdabb6
Revises: d2fa46fe573c
Create Date: 2022-04-25 17:51:18.590834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97b2cbbdabb6'
down_revision = 'd2fa46fe573c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('url_shortner', sa.Column('note', sa.String(length=512), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('url_shortner', 'note')
    # ### end Alembic commands ###
