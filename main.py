from fastapi import FastAPI
import uvicorn
from routes.transactions_routes import transaction_app
from database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

# Criar tabelas no banco de dados, se ainda não existirem
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def retornaralgo():
    return "Home"


# Incluir roteador de transações
app.include_router(transaction_app)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
