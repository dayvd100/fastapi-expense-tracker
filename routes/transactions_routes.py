from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.transactions_schemas import TransactionCreate, TransactionSchema
from crud.transactions_crud import (
    create_transaction,
    delete_transaction,
    get_transaction,
    get_transactions,
)
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


@transaction_app.get("/transactions", response_model=list[TransactionSchema])
def get_transactions_endpoint(db: Session = Depends(get_db)):
    return get_transactions(db=db)


@transaction_app.get("/transactions/{transaction_id}")
def get_transaction_by_id(transaction_id, db: Session = Depends(get_db)):
    transaction = get_transaction(db=db, transaction_id=transaction_id)
    if transaction:
        return transaction
    else:
        return {"Transaction not found"}


@transaction_app.delete("/transactions/{transaction_id}", response_model=dict)
def delete_transaction_endpoint(transaction_id: int, db: Session = Depends(get_db)):
    result = delete_transaction(db=db, transaction_id=transaction_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result
