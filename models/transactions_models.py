from sqlalchemy import Column, Float, Integer, String
from database import Base


class Transactions(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount_transaction = Column(Float, nullable=False)
    name_transaction = Column(String(255), nullable=False)
