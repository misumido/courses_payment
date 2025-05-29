from sqlalchemy import (Column, Integer,
                        String, DateTime)
from database import Base

class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    tg_id = Column(Integer)
    phone_number = Column(String)
    product = Column(String)
    payment_date = Column(String)



