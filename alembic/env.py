import asyncio
from logging.config import fileConfig

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from alembic import context

from app.core.config import settings
from app.db.base import Base  # Base declarativa com todos os modelos importados

# Carregar configurações do alembic.ini
config = context.config
fileConfig(config.config_file_name)

# Database URL convertida para o driver async
DATABASE_URL = settings.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")

# Metadados que o Alembic vai usar para autogenerate
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Executa migrações no modo offline (gera SQL sem aplicar)."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()

def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata, compare_type=True)

    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online() -> None:
    """Executa migrações no modo online (aplica no banco)."""
    connectable: AsyncEngine = create_async_engine(DATABASE_URL, poolclass=None)

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()

if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
