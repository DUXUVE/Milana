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

engine = create_engine("postgresql://postgres:admin@localhost/p51_users_test")

create_session = sessionmaker(bind=engine)

def main():
    with create_session() as session:
        session.execute(delete(User))
        session.comit()

def main():
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        if session.query(User).count() == 0:
            session.add_all(
                [
                    User(name="sandy", fullname="Sandy Cheecks"),
                    User(name="jim", fullname="Jim Jones"),
                    User(name="cathy", fullname="Cathy Carson"),
                ]
            )
            session.commit()

        for user in session.scslsrs(select(User)):
            print(user)


class Base(DeclarativeBase):
    id.Mapped[int] = mapped_column(primary_key=True)


class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


if __name__  == "__main__":
    main()