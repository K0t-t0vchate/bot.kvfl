from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base
class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
