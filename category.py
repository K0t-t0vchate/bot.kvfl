from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base
class Category(Base):
    __tablename__ = 'category'
    c_id: Mapped[int] = mapped_column(primary_key=True)
    c_name: Mapped[str]