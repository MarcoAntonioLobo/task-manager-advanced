# 🧠 Task Manager Advanced

Uma aplicação moderna e completa para **gerenciamento de tarefas**, construída com tecnologias de ponta do ecossistema Python. Ideal para estudos, projetos profissionais e deploys escaláveis.

---

## 🚀 Tecnologias Utilizadas

- **FastAPI (async)** – Framework web moderno e rápido  
- **PostgreSQL + SQLAlchemy 2.0 (async)** – Banco de dados relacional e ORM  
- **Alembic** – Migrações do banco de dados  
- **Docker & Docker Compose** – Containerização e orquestração  
- **Python 3.12** – Linguagem principal  
- **Redis + Celery** – Fila e execução de tarefas assíncronas  
- **Pydantic v2 + pydantic-settings** – Validação e configuração de ambiente  
- **Flower** – Interface gráfica para monitoramento das tarefas Celery

---

## 📁 Estrutura do Projeto
``` 
task-manager-advanced/
├── app/
│ ├── api/ # Rotas da API
│ ├── core/ # Configurações da aplicação
│ ├── db/ # Conexão com o banco de dados
│ ├── models/ # Modelos SQLAlchemy
│ ├── schemas/ # Schemas Pydantic
│ ├── services/ # Regras de negócio
│ ├── tasks/ # Tarefas Celery
│ └── main.py # Entrypoint da API
├── alembic/ # Migrações Alembic
├── tests/ # Testes automatizados
├── Dockerfile # Imagem Docker da aplicação
├── docker-compose.yml
├── requirements.txt
├── .env.example # Modelo de variáveis de ambiente
└── README.md
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

```bash

cp .env.example .env
```
Edite o .env com as suas configurações:

```env

# PostgreSQL
POSTGRES_USER=malobo
POSTGRES_PASSWORD=233234
POSTGRES_DB=taskdb
POSTGRES_HOST=db
POSTGRES_PORT=5432

# Redis
REDIS_HOST=redis
REDIS_PORT=6379
```
3. Subir com Docker (recomendado)
```bash

docker compose up --build -d
```
4. Executar as migrações
```bash

docker compose exec web alembic revision --autogenerate -m "criação inicial"
docker compose exec web alembic upgrade head
```
5. Acessos disponíveis
Serviço	URL
API FastAPI	http://localhost:8000
Documentação	http://localhost:8000/docs
Monitor Celery (Flower)	http://localhost:5555

✅ Rodar sem Docker (para desenvolvimento)

```bash

python -m venv venv
source venv/bin/activate        # Linux/macOS
# venv\Scripts\activate.bat     # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```
📦 Dependências Principais
```text

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
```
Instale com:

```bash

pip install -r requirements.txt
```
🧪 Endpoints de Exemplo
| Método | Rota        | Descrição                   |
|--------|-------------|-----------------------------|
| GET    | /tasks      | Lista todas as tarefas      |
| POST   | /tasks      | Cria uma nova tarefa        |
| PUT    | /tasks/{id} | Edita uma tarefa pelo ID    |
| DELETE | /tasks/{id} | Remove uma tarefa pelo ID   |
| GET    | /health     | Healthcheck do container    |


💡 Para que serve essa aplicação?
O Task Manager Advanced é uma API REST para gerenciar tarefas de forma eficiente.
Foi criada para demonstrar boas práticas modernas de desenvolvimento com:

Backend assíncrono com FastAPI

Banco de dados relacional com PostgreSQL

Execução de tarefas em background com Redis + Celery

Deploy simplificado via Docker

Monitoramento com Flower

Ideal para uso real, aprendizado ou portfólio.

🚀 Autor
Marco Antônio Lobo
📧 marcoantoniolobo82@gmail.com

🤝 Contribuições
Gostou do projeto?
Faça um fork, contribua com PRs, sugestões ou melhorias.
Contribuições são sempre bem-vindas!