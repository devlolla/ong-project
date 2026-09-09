# Guardiões da Causa Animal

Sistema interno de gestão para a ONG Guardiões da Causa Animal.

## Tecnologias

- Python 3.10
- Django 5.2 LTS
- Django Templates
- PostgreSQL
- HTMX — será adicionado nas fases de interface

## Configuração local

1. Clone o repositório e entre na pasta do projeto.

2. Crie e ative o ambiente virtual:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Execute as migrações:

   ```bash
   python manage.py migrate
   ```

5. Inicie o servidor:

   ```bash
   python manage.py runserver
   ```

A aplicação estará disponível em `http://127.0.0.1:8000/`.

## Testes

```bash
python manage.py test
```

## PostgreSQL local

1. Instale o PostgreSQL.

2. Crie o usuário e o banco da aplicação:

   ```bash
   sudo -u postgres createuser --pwprompt ong_user
   sudo -u postgres createdb --owner=ong_user --encoding=UTF8 ong_project
   ```

3. Crie um arquivo .env na raiz do projeto com base em .env.example e informe suas credenciais locais.

4. Execute as migrações:

```bash
python manage.py migrate
```

## Ambiente Docker

O projeto também pode ser executado com Docker Compose. Essa opção inicia o Django e o PostgreSQL em containers, sem depender da `.venv` ou do PostgreSQL instalados localmente.

### 1. Crie o arquivo de variáveis Docker

```bash
cp .env.docker.example .env.docker
```

Edite `.env.docker` e informe uma chave secreta e uma senha de desenvolvimento.

### 2. Inicie os containers

Na primeira execução, ou após alterar `Dockerfile` ou `requirements.txt`:

```bash
docker compose up --build
```

Nas próximas execuções:

```bash
docker compose up
```

A aplicação estará disponível em `http://127.0.0.1:8000/`.

### 3. Execute as migrations

Em outro terminal:

```bash
docker compose exec web python manage.py migrate
```

### 4. Execute os testes

```bash
docker compose exec web python manage.py test
```

### Comandos úteis

Verificar o estado dos containers:

```bash
docker compose ps
```

Acompanhar os logs do Django:

```bash
docker compose logs -f web
```

Parar os containers sem apagar os dados do banco:

```bash
docker compose down
```

> Atenção: `docker compose down -v` também remove o volume `postgres_data` e apaga todos os dados do PostgreSQL Docker.
