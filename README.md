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
   ``

3. Crie um arquivo .env na raiz do projeto com base em .env.example e informe suas credenciais locais.

4. Execute as migrações:

```bash
python manage.py migrate
```
