from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from models.base import Base
class Book(Base):
    __tablename__ = 'book'
    b_id: Mapped[int] = mapped_column(primary_key=True)
    b_name: Mapped[str]
    catId: Mapped[int] = mapped_column(ForeignKey('category.c_id'))