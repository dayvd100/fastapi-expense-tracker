from pydantic import BaseModel


class TransactionCreate(BaseModel):
    amount_transaction: float
    name_transaction: str


class TransactionSchema(BaseModel):
    id: int
    amount_transaction: float
    name_transaction: str

    class Config:
        orm_mode = True
