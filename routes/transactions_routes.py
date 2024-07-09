from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.transactions_schemas import TransactionCreate, TransactionSchema
from crud.transactions_crud import create_transaction, get_transactions
from database import get_db

transaction_app = APIRouter()


@transaction_app.post("/transaction", response_model=TransactionSchema)
def create_transaction_endpoint(
    transaction: TransactionCreate,
    db: Session = Depends(get_db),
):
    return create_transaction(
        db=db,
        transaction=transaction,
    )


@transaction_app.get("/transactions")
def get_transactions_endpoint(db: Session = Depends(get_db)):
    return get_transactions(db=db)
