from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy import select, delete, update

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    def __repr__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.price}, quantity={self.quantity})"

engine = create_engine("sqlite:///electronics.db")
Base.metadata.create_all(engine)

with Session(engine) as session:
    session.add_all([
        Product(name="Laptop", price=1200.50, quantity=5),
        Product(name="Phone", price=800.00, quantity=10),
        Product(name="Tablet", price=300.00, quantity=0)
    ])
    session.commit()
    
    stmt = update(Product).where(Product.name == "Laptop").values(quantity=10)
    session.execute(stmt)
    
    stmt = delete(Product).where(Product.quantity == 0)
    session.execute(stmt)
    
    session.commit()
    
    stmt = select(Product)
    results = session.execute(stmt).scalars().all()

    output = [(p.id, p.name, p.price, p.quantity) for p in results]
    print(output)