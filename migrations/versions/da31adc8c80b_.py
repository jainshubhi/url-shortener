"""empty message

Revision ID: da31adc8c80b
Revises: 099d24ed2c91
Create Date: 2016-03-05 02:43:44.526135

"""

# revision identifiers, used by Alembic.
revision = 'da31adc8c80b'
down_revision = '099d24ed2c91'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('urls', sa.Column('url_shortened', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('urls', 'url_shortened')
    ### end Alembic commands ###
