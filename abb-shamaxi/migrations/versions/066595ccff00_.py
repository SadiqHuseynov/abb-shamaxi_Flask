"""empty message

Revision ID: 066595ccff00
Revises: 973b4b470549
Create Date: 2023-10-24 09:50:30.311738

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '066595ccff00'
down_revision = '973b4b470549'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('company', schema=None) as batch_op:
        batch_op.alter_column('button',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.String(length=50),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('company', schema=None) as batch_op:
        batch_op.alter_column('button',
               existing_type=sa.String(length=50),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)

    # ### end Alembic commands ###
