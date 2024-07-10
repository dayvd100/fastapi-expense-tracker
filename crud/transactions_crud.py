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


def get_transaction(db: Session, transaction_id: int):
    db_transaction = (
        db.query(Transactions).filter(Transactions.id == transaction_id).first()
    )
    return db_transaction


def delete_transaction(db: Session, transaction_id: int):
    db_transaction = (
        db.query(Transactions).filter(Transactions.id == transaction_id).first()
    )
    if db_transaction:
        db.delete(db_transaction)
        db.commit()
        return {"message": "Transaction deleted successfully"}
    else:
        return {"error": "Transaction not found"}
