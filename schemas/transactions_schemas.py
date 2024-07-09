from pydantic import BaseModel


class TransactionBase(BaseModel):
    name_transaction: str
    amount_transaction: float


class TransactionCreate(TransactionBase):
    pass


class TransactionSchema(TransactionBase):
    id: int

    class Config:
        orm_mode = True
