from fastapi import FastAPI
from routes.transactions_routes import transaction_app
from database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

# Criar tabelas no banco de dados, se ainda não existirem
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Aqui você pode configurar os domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def retornaralgo():
    return "Home"


# Incluir roteador de transações
app.include_router(transaction_app)
