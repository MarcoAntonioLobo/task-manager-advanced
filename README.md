# 🧠 Task Manager Advanced

Uma aplicação moderna e completa para **gerenciamento de tarefas**, construída para ser rápida, escalável e fácil de usar, usando as tecnologias mais atuais do ecossistema Python.

---

## 🚀 Tecnologias Utilizadas

- **FastAPI (async)** – Framework web moderno e rápido  
- **PostgreSQL + SQLAlchemy 2.0 (async)** – Banco de dados relacional e ORM  
- **Alembic** – Ferramenta de migrações para banco  
- **Docker & Docker Compose** – Containerização e orquestração  
- **Python 3.12** – Linguagem principal  
- **Redis + Celery** – Execução de tarefas assíncronas e filas  
- **Pydantic v2 + pydantic-settings** – Validação e configuração

---

## 📁 Estrutura do Projeto
```
task_manager_advanced/
├── app/
│ ├── api/ # Rotas da API (endpoints)
│ ├── core/ # Configurações (pydantic-settings)
│ ├── db/ # Engine e sessão do banco (SQLAlchemy)
│ ├── models/ # Modelos ORM (SQLAlchemy)
│ ├── schemas/ # Schemas de validação (Pydantic)
│ ├── services/ # Regras de negócio e lógica da aplicação
│ ├── tasks/ # Tarefas assíncronas Celery
│ └── main.py # Entrypoint da API FastAPI
├── alembic/ # Migrações do banco de dados (Alembic)
├── tests/ # Testes automatizados
├── Dockerfile # Imagem Docker da aplicação
├── docker-compose.yml # Orquestração dos containers
├── requirements.txt # Dependências Python
├── .env.example # Exemplo de variáveis de ambiente
└── README.md # Documentação do projeto
```
yaml

---

## ⚙️ Configuração e Execução

### 1. Clonar o repositório

```bash
git clone https://github.com/MarcoAntonioLobo/task-manager-advanced.git
cd task-manager-advanced
```
2. Criar o arquivo .env
Copie o modelo e edite com seus dados:

```bash

cp .env.example .env
```
Edite .env com suas configurações, exemplo:

```env

POSTGRES_USER=malobo
POSTGRES_PASSWORD=233234
POSTGRES_DB=taskdb
POSTGRES_HOST=db
POSTGRES_PORT=5432

REDIS_HOST=redis
REDIS_PORT=6379
```
3. Rodar com Docker (recomendado)
Suba os containers:

```bash

docker compose up --build -d
```
Rode as migrações do banco:

```bash

docker compose exec web alembic revision --autogenerate -m "criação inicial"
docker compose exec web alembic upgrade head
```
4. Rodar localmente sem Docker (para desenvolvimento)

```bash

python -m venv venv
source venv/bin/activate      # Linux/macOS
# venv\Scripts\activate.bat   # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```
📦 Dependências Principais
fastapi

uvicorn[standard]

sqlalchemy==2.0.*

asyncpg

alembic

pydantic

pydantic-settings

python-dotenv

passlib[bcrypt]

pyjwt

redis

celery

Instale com:

```bash

pip install -r requirements.txt
```
🧪 Endpoints de Exemplo
```
| Método | Rota          | Descrição                 |
|--------|---------------|---------------------------|
| GET    | /tasks        | Lista todas as tarefas    |
| POST   | /tasks        | Cria uma nova tarefa      |
| PUT    | /tasks/{id}   | Edita uma tarefa pelo ID  |
| DELETE | /tasks/{id}   | Remove uma tarefa pelo ID |
```
💡 Para que serve essa aplicação?
O Task Manager Advanced é uma ferramenta para ajudar pessoas e equipes a organizar, criar, acompanhar e gerenciar tarefas de forma eficiente, usando:

Interface via API REST (com FastAPI) para criar, ler, atualizar e apagar tarefas

Banco de dados PostgreSQL para armazenar as informações

Redis + Celery para processar tarefas demoradas em background (exemplo: notificações, emails)

Totalmente containerizada via Docker para facilitar deploy e desenvolvimento

🚀 Autor
Marco Antônio Lobo
📧 marcoantoniolobo82@gmail.com

Gostou do projeto? Quer colaborar?
Faça um fork, abra issues ou PRs!
Contribuições são muito bem-vindas!