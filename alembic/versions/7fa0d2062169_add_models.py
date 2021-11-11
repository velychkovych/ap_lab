"""add models

Revision ID: 7fa0d2062169
Revises: c23526991611
Create Date: 2021-11-11 17:35:30.364642

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7fa0d2062169'
down_revision = 'c23526991611'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userStatus',
    sa.Column('idUserStatus', sa.Integer(), nullable=False),
    sa.Column('status', sa.VARCHAR(length=45), nullable=True),
    sa.PrimaryKeyConstraint('idUserStatus')
    )
    op.create_table('user',
    sa.Column('idUser', sa.Integer(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=45), nullable=True),
    sa.Column('firstname', sa.VARCHAR(length=45), nullable=True),
    sa.Column('lastname', sa.VARCHAR(length=45), nullable=True),
    sa.Column('email', sa.VARCHAR(length=45), nullable=True),
    sa.Column('password', sa.VARCHAR(length=45), nullable=True),
    sa.Column('dateOfRegistration', sa.DateTime(), nullable=True),
    sa.Column('idUserStatus', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['idUserStatus'], ['userStatus.idUserStatus'], ),
    sa.PrimaryKeyConstraint('idUser'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('article',
    sa.Column('idArticle', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('header', sa.VARCHAR(length=45), nullable=True),
    sa.Column('textOfArticle', sa.VARCHAR(length=2000), nullable=True),
    sa.Column('idAuthor', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['idAuthor'], ['user.idUser'], ),
    sa.PrimaryKeyConstraint('idArticle')
    )
    op.create_table('modification',
    sa.Column('idModification', sa.Integer(), nullable=False),
    sa.Column('dateOfModification', sa.DateTime(), nullable=True),
    sa.Column('idUser', sa.Integer(), nullable=True),
    sa.Column('idArticle', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['idArticle'], ['article.idArticle'], ),
    sa.ForeignKeyConstraint(['idUser'], ['user.idUser'], ),
    sa.PrimaryKeyConstraint('idModification')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('modification')
    op.drop_table('article')
    op.drop_table('user')
    op.drop_table('userStatus')
    # ### end Alembic commands ###