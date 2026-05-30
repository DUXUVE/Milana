import select
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, create_engine, delete
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
    

class Product(Base):
    __tablename__ = "products" 
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    # description: Mapped[str] = mapped_column(String(255), nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    category_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("categories.id", ondelete="set null"))
    category: Mapped["Category"] = relationship(back_populates="products")


class Category(Base):
    __tablename__ = "categories"
    name: Mapped[str] = mapped_column(String(255))
    products: Mapped[list["Product"]] = relationship(back_populates="category")