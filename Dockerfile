# Usar Python oficial
FROM python:3.11-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar Poetry
RUN pip install poetry==1.8.3

# Criar diretório de trabalho
WORKDIR /app

# Copiar arquivos de configuração
COPY pyproject.toml poetry.lock* ./

# Instalar dependências (sem --with dev)
RUN poetry install --no-root

# Copiar projeto
COPY . .

# Expor porta padrão do Django
EXPOSE 8000

# Comando para rodar o servidor
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
