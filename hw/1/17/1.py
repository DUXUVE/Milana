from sqlalchemy import ForeignKey, String, Integer, Date, DateTime, Text, func, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import Optional, List

class Base(DeclarativeBase):
    pass

class Author(Base):
    __tablename__ = "authors"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    birth_date: Mapped[Optional[Date]] = mapped_column(Date, nullable=True)
    books: Mapped[List["Book"]] = relationship(
        "Book", back_populates="author", cascade="save-update, merge"
    )

class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    publication_year: Mapped[int] = mapped_column(Integer, nullable=False)
    isbn: Mapped[Optional[str]] = mapped_column(String(17), unique=True, nullable=True)
    author_id: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey("authors.id", ondelete="SET NULL"), nullable=True)
    
    author: Mapped[Optional["Author"]] = relationship("Author", back_populates="books")
    reviews: Mapped[List["Review"]] = relationship(
        "Review", 
        back_populates="book",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

class Review(Base):
    __tablename__ = "reviews"
    __table_args__ = (CheckConstraint('rating >= 1 AND rating <= 5', name='check_rating_range'),)
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)
    book_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("books.id", ondelete="CASCADE"), nullable=False)
    date: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
    book: Mapped["Book"] = relationship("Book", back_populates="reviews")