from sqlalchemy import create_engine
from sqlalchemy import Base
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String

engine = create_engine("sqlite:///database/db.db", echo=True)

def create_db_and_tables() -> None:
	Base.metadata.create_all(engine)
	
class UserBase(Base):
	__tablename__ = "Adress"

	id: Mapped[int] = mapped_column(primary_key=True)
	adress: Mapped[str] = mapped_column(String(30))
	
