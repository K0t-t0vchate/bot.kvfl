from sqlalchemy import select

from connect.db import Session
from models.book import Book
from models.category import Category


class MessageController:

    select(Book).select_from(Book).where(Book.id==4).all()
    session = Session

    @classmethod
    def get_book_by_category(cls, category):
        query = (
            select(Book.b_name).select_from(Book).join(Category, Book.catId == Category.c_id).where(Category.c_name == category)
        )
        with cls.session.begin() as session:
            return session.execute(query).scalars().all()