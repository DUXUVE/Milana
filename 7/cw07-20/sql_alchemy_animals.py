from datetime import datetime
from typing import List
from sqlalchemy import (
    String, Integer, BigInteger, ForeignKey, 
    DateTime, func, CheckConstraint, UniqueConstraint,
    create_engine, select, insert
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker


def main():
    engine = create_engine(
        'sqlite:///animals.db')

    create_session = sessionmaker(bind=engine)

    with create_session() as session:
        Base.metadata.create_all(engine)
        seed_data(session)
        print(session.execute(select(Animal.id)).all())

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)


class Voliere(Base):
    __tablename__ = "volieres"
    
    status: Mapped[str] = mapped_column(String(50), nullable=False)
    last_clean: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.current_timestamp()
    )

    # Связи (optional, для удобства ORM)
    animals: Mapped[List["Animal"]] = relationship(back_populates="voliere")
    cleanings: Mapped[List["Cleaning"]] = relationship(back_populates="voliere")


class Employee(Base):
    __tablename__ = "employees"
    
    
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    role: Mapped[str] = mapped_column(String(50), nullable=False)

    cleanings: Mapped[List["Cleaning"]] = relationship(back_populates="employee")
    feedings: Mapped[List["Feeding"]] = relationship(back_populates="employee")
    responsibilities: Mapped[List["AnimalEmployeeResponsible"]] = relationship(back_populates="employee")


class Animal(Base):
    __tablename__ = "animals"
    __table_args__ = (
        CheckConstraint("age >= 0", name="check_animal_age_positive"),
    )
    
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    voliere_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("volieres.id"), nullable=False)

    voliere: Mapped["Voliere"] = relationship(back_populates="animals")
    feedings: Mapped[List["Feeding"]] = relationship(back_populates="animal")
    responsibles: Mapped[List["AnimalEmployeeResponsible"]] = relationship(back_populates="animal")


class Cleaning(Base):
    __tablename__ = "cleanings"
    
    date: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.current_timestamp()
    )
    employee_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("employees.id"), nullable=False)
    voliere_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("volieres.id"), nullable=False)

    employee: Mapped["Employee"] = relationship(back_populates="cleanings")
    voliere: Mapped["Voliere"] = relationship(back_populates="cleanings")


class Feeding(Base):
    __tablename__ = "feedings"
    
    date: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.current_timestamp()
    )
    animal_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("animals.id"), nullable=False)
    employee_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("employees.id"), nullable=False)

    animal: Mapped["Animal"] = relationship(back_populates="feedings")
    employee: Mapped["Employee"] = relationship(back_populates="feedings")


class AnimalEmployeeResponsible(Base):
    __tablename__ = "animal_employee_responsibles"
    __table_args__ = (
        UniqueConstraint("animal_id", "employee_id", name="uq_animal_employee"),
    )
    
    animal_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("animals.id"), nullable=False)
    employee_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("employees.id"), nullable=False)
    date: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.current_timestamp()
    )

    animal: Mapped["Animal"] = relationship(back_populates="responsibles")
    employee: Mapped["Employee"] = relationship(back_populates="responsibilities")


def seed_data(session):
    # Volieres
    session.execute(insert(Voliere), [
        {"status": "active", "last_clean": datetime(2026, 7, 1, 10, 0)},
        {"status": "active", "last_clean": datetime(2026, 7, 2, 11, 30)},
        {"status": "maintenance", "last_clean": datetime(2026, 6, 28, 9, 0)},
        {"status": "active", "last_clean": datetime(2026, 7, 3, 14, 0)},
        {"status": "active", "last_clean": datetime(2026, 7, 4, 8, 30)},
        {"status": "closed", "last_clean": datetime(2026, 6, 25, 16, 0)},
        {"status": "active", "last_clean": datetime(2026, 7, 5, 12, 0)},
        {"status": "active", "last_clean": datetime(2026, 7, 6, 10, 30)},
        {"status": "maintenance", "last_clean": datetime(2026, 6, 30, 15, 0)},
        {"status": "active", "last_clean": datetime(2026, 7, 7, 9, 30)},
    ])

    # Employees
    session.execute(insert(Employee), [
        {"name": "Иванов Иван", "role": "zookeeper"},
        {"name": "Петрова Анна", "role": "veterinarian"},
        {"name": "Сидоров Петр", "role": "cleaner"},
        {"name": "Козлова Мария", "role": "zookeeper"},
        {"name": "Новиков Алексей", "role": "veterinarian"},
        {"name": "Морозова Елена", "role": "cleaner"},
        {"name": "Волков Дмитрий", "role": "zookeeper"},
        {"name": "Лебедева Ольга", "role": "cleaner"},
        {"name": "Соколов Андрей", "role": "veterinarian"},
        {"name": "Попова Татьяна", "role": "zookeeper"},
    ])

    # Animals
    session.execute(insert(Animal), [
        {"name": "Лев Симба", "age": 5, "voliere_id": 1},
        {"name": "Тигр Шерхан", "age": 7, "voliere_id": 1},
        {"name": "Слон Джамбо", "age": 12, "voliere_id": 2},
        {"name": "Жираф Мелман", "age": 8, "voliere_id": 2},
        {"name": "Зебра Марти", "age": 4, "voliere_id": 3},
        {"name": "Обезьяна Кинг", "age": 6, "voliere_id": 3},
        {"name": "Медведь Балу", "age": 9, "voliere_id": 4},
        {"name": "Волк Акела", "age": 5, "voliere_id": 4},
        {"name": "Панда По", "age": 3, "voliere_id": 5},
        {"name": "Кенгуру Рокки", "age": 4, "voliere_id": 5},
        {"name": "Лиса Алиса", "age": 2, "voliere_id": 6},
        {"name": "Заяц Багз", "age": 1, "voliere_id": 6},
        {"name": "Орел Сокол", "age": 10, "voliere_id": 7},
        {"name": "Попугай Кеша", "age": 15, "voliere_id": 7},
        {"name": "Пингвин Пинго", "age": 6, "voliere_id": 8},
        {"name": "Тюлень Немо", "age": 3, "voliere_id": 8},
        {"name": "Крокодил Гена", "age": 20, "voliere_id": 9},
        {"name": "Бегемот Мотя", "age": 11, "voliere_id": 9},
        {"name": "Рысь Мурка", "age": 4, "voliere_id": 10},
        {"name": "Ежик Соник", "age": 2, "voliere_id": 10},
    ])

    # Cleanings
    session.execute(insert(Cleaning), [
        {"date": datetime(2026, 7, 1, 8, 0), "employee_id": 3, "voliere_id": 1},
        {"date": datetime(2026, 7, 1, 9, 30), "employee_id": 6, "voliere_id": 2},
        {"date": datetime(2026, 7, 1, 11, 0), "employee_id": 8, "voliere_id": 3},
        {"date": datetime(2026, 7, 2, 8, 0), "employee_id": 3, "voliere_id": 4},
        {"date": datetime(2026, 7, 2, 9, 30), "employee_id": 6, "voliere_id": 5},
        {"date": datetime(2026, 7, 2, 11, 0), "employee_id": 8, "voliere_id": 6},
        {"date": datetime(2026, 7, 3, 8, 0), "employee_id": 3, "voliere_id": 7},
        {"date": datetime(2026, 7, 3, 9, 30), "employee_id": 6, "voliere_id": 8},
        {"date": datetime(2026, 7, 3, 11, 0), "employee_id": 8, "voliere_id": 9},
        {"date": datetime(2026, 7, 4, 8, 0), "employee_id": 3, "voliere_id": 10},
        {"date": datetime(2026, 7, 4, 9, 30), "employee_id": 6, "voliere_id": 1},
        {"date": datetime(2026, 7, 4, 11, 0), "employee_id": 8, "voliere_id": 2},
        {"date": datetime(2026, 7, 5, 8, 0), "employee_id": 3, "voliere_id": 3},
        {"date": datetime(2026, 7, 5, 9, 30), "employee_id": 6, "voliere_id": 4},
        {"date": datetime(2026, 7, 5, 11, 0), "employee_id": 8, "voliere_id": 5},
        {"date": datetime(2026, 7, 6, 8, 0), "employee_id": 3, "voliere_id": 6},
        {"date": datetime(2026, 7, 6, 9, 30), "employee_id": 6, "voliere_id": 7},
        {"date": datetime(2026, 7, 6, 11, 0), "employee_id": 8, "voliere_id": 8},
        {"date": datetime(2026, 7, 7, 8, 0), "employee_id": 3, "voliere_id": 9},
        {"date": datetime(2026, 7, 7, 9, 30), "employee_id": 6, "voliere_id": 10},
        {"date": datetime(2026, 7, 7, 11, 0), "employee_id": 8, "voliere_id": 1},
        {"date": datetime(2026, 7, 8, 8, 0), "employee_id": 3, "voliere_id": 2},
        {"date": datetime(2026, 7, 8, 9, 30), "employee_id": 6, "voliere_id": 3},
        {"date": datetime(2026, 7, 8, 11, 0), "employee_id": 8, "voliere_id": 4},
        {"date": datetime(2026, 7, 9, 8, 0), "employee_id": 3, "voliere_id": 5},
        {"date": datetime(2026, 7, 9, 9, 30), "employee_id": 6, "voliere_id": 6},
        {"date": datetime(2026, 7, 9, 11, 0), "employee_id": 8, "voliere_id": 7},
        {"date": datetime(2026, 7, 10, 8, 0), "employee_id": 3, "voliere_id": 8},
        {"date": datetime(2026, 7, 10, 9, 30), "employee_id": 6, "voliere_id": 9},
        {"date": datetime(2026, 7, 10, 11, 0), "employee_id": 8, "voliere_id": 10},
    ])

    # Feedings
    session.execute(insert(Feeding), [
        {"date": datetime(2026, 7, 1, 7, 0), "animal_id": 1, "employee_id": 1},
        {"date": datetime(2026, 7, 1, 7, 30), "animal_id": 2, "employee_id": 1},
        {"date": datetime(2026, 7, 1, 8, 0), "animal_id": 3, "employee_id": 4},
        {"date": datetime(2026, 7, 1, 8, 30), "animal_id": 4, "employee_id": 4},
        {"date": datetime(2026, 7, 1, 9, 0), "animal_id": 5, "employee_id": 7},
        {"date": datetime(2026, 7, 1, 9, 30), "animal_id": 6, "employee_id": 7},
        {"date": datetime(2026, 7, 2, 7, 0), "animal_id": 7, "employee_id": 1},
        {"date": datetime(2026, 7, 2, 7, 30), "animal_id": 8, "employee_id": 1},
        {"date": datetime(2026, 7, 2, 8, 0), "animal_id": 9, "employee_id": 4},
        {"date": datetime(2026, 7, 2, 8, 30), "animal_id": 10, "employee_id": 4},
        {"date": datetime(2026, 7, 2, 9, 0), "animal_id": 11, "employee_id": 7},
        {"date": datetime(2026, 7, 2, 9, 30), "animal_id": 12, "employee_id": 7},
        {"date": datetime(2026, 7, 3, 7, 0), "animal_id": 13, "employee_id": 1},
        {"date": datetime(2026, 7, 3, 7, 30), "animal_id": 14, "employee_id": 1},
        {"date": datetime(2026, 7, 3, 8, 0), "animal_id": 15, "employee_id": 4},
        {"date": datetime(2026, 7, 3, 8, 30), "animal_id": 16, "employee_id": 4},
        {"date": datetime(2026, 7, 3, 9, 0), "animal_id": 17, "employee_id": 7},
        {"date": datetime(2026, 7, 3, 9, 30), "animal_id": 18, "employee_id": 7},
        {"date": datetime(2026, 7, 4, 7, 0), "animal_id": 19, "employee_id": 1},
        {"date": datetime(2026, 7, 4, 7, 30), "animal_id": 20, "employee_id": 1},
        {"date": datetime(2026, 7, 4, 8, 0), "animal_id": 1, "employee_id": 4},
        {"date": datetime(2026, 7, 4, 8, 30), "animal_id": 2, "employee_id": 4},
        {"date": datetime(2026, 7, 5, 7, 0), "animal_id": 3, "employee_id": 7},
        {"date": datetime(2026, 7, 5, 7, 30), "animal_id": 4, "employee_id": 7},
        {"date": datetime(2026, 7, 5, 8, 0), "animal_id": 5, "employee_id": 1},
        {"date": datetime(2026, 7, 5, 8, 30), "animal_id": 6, "employee_id": 1},
        {"date": datetime(2026, 7, 6, 7, 0), "animal_id": 7, "employee_id": 4},
        {"date": datetime(2026, 7, 6, 7, 30), "animal_id": 8, "employee_id": 4},
        {"date": datetime(2026, 7, 6, 8, 0), "animal_id": 9, "employee_id": 7},
        {"date": datetime(2026, 7, 6, 8, 30), "animal_id": 10, "employee_id": 7},
        {"date": datetime(2026, 7, 7, 7, 0), "animal_id": 11, "employee_id": 1},
        {"date": datetime(2026, 7, 7, 7, 30), "animal_id": 12, "employee_id": 1},
        {"date": datetime(2026, 7, 7, 8, 0), "animal_id": 13, "employee_id": 4},
        {"date": datetime(2026, 7, 7, 8, 30), "animal_id": 14, "employee_id": 4},
        {"date": datetime(2026, 7, 8, 7, 0), "animal_id": 15, "employee_id": 7},
        {"date": datetime(2026, 7, 8, 7, 30), "animal_id": 16, "employee_id": 7},
        {"date": datetime(2026, 7, 8, 8, 0), "animal_id": 17, "employee_id": 1},
        {"date": datetime(2026, 7, 8, 8, 30), "animal_id": 18, "employee_id": 1},
        {"date": datetime(2026, 7, 9, 7, 0), "animal_id": 19, "employee_id": 4},
        {"date": datetime(2026, 7, 9, 7, 30), "animal_id": 20, "employee_id": 4},
        {"date": datetime(2026, 7, 9, 8, 0), "animal_id": 1, "employee_id": 7},
        {"date": datetime(2026, 7, 9, 8, 30), "animal_id": 2, "employee_id": 7},
        {"date": datetime(2026, 7, 10, 7, 0), "animal_id": 3, "employee_id": 1},
        {"date": datetime(2026, 7, 10, 7, 30), "animal_id": 4, "employee_id": 1},
        {"date": datetime(2026, 7, 10, 8, 0), "animal_id": 5, "employee_id": 4},
        {"date": datetime(2026, 7, 10, 8, 30), "animal_id": 6, "employee_id": 4},
        {"date": datetime(2026, 7, 10, 9, 0), "animal_id": 7, "employee_id": 7},
        {"date": datetime(2026, 7, 10, 9, 30), "animal_id": 8, "employee_id": 7},
        {"date": datetime(2026, 7, 10, 10, 0), "animal_id": 9, "employee_id": 1},
        {"date": datetime(2026, 7, 10, 10, 30), "animal_id": 10, "employee_id": 1},
    ])

    # Animal Employee Responsibles
    session.execute(insert(AnimalEmployeeResponsible), [
        {"animal_id": 1, "employee_id": 1, "date": datetime(2026, 7, 1, 6, 0)},
        {"animal_id": 2, "employee_id": 1, "date": datetime(2026, 7, 1, 6, 0)},
        {"animal_id": 3, "employee_id": 4, "date": datetime(2026, 7, 1, 6, 0)},
        {"animal_id": 4, "employee_id": 4, "date": datetime(2026, 7, 1, 6, 0)},
        {"animal_id": 5, "employee_id": 7, "date": datetime(2026, 7, 1, 6, 0)},
    ])


if __name__ == "__main__":
    main()