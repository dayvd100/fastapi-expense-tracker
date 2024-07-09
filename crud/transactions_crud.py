from sqlalchemy.orm import Session
from models.transactions_models import Transactions
from schemas.transactions_schemas import TransactionCreate


def create_transaction(db: Session, transaction: TransactionCreate):
    db_transaction = Transactions(**transaction.model_dump())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


def get_transactions(db: Session):
    return db.query(Transactions).all()
