
from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

engine = create_engine("postgresql+psycopg2://postgres:admin@localhost:5432/postgres", echo=True)
Session = sessionmaker(engine)