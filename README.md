# 

# Cервис Greetings traveller

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat-square&logo=SQLAlchemy)](https://www.sqlalchemy.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![Gunicorn](https://img.shields.io/badge/-Gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)


## Описание

- Раздел с материалами по миграции данных
- Раздел c материалами для архитектуры базы данных
- Раздел с материалами по миграции данных


#### Технологии

- Python 3.12
- Docker
- PostgreSQL
- Gunicorn

#### Локальный запуск проекта

- Склонировать репозиторий:

```bash
    git clone <название репозитория>
```

Cоздать и активировать виртуальное окружение:

Команды для установки виртуального окружения на Mac или Linux:

```bash
    python3 -m venv env
    source env/bin/activate
```

Команды для Windows:

```bash
    python -m venv venv
    source venv/Scripts/activate

```

- Перейти в директорию movies_admin:

```bash
    cd /movies_admin
```

- Создать файл .env по образцу:

```bash
    cp .env.example .env

```
- Перейти в директорию sqlite_to_postgres:

```bash
    cd /sqlite_to_postgres
```

- Создать файл .env по образцу:

```bash
    cp .env.example.local .env
```

- Установить зависимости из файла requirements.txt в главной папке проекта:

```bash
    cd ..
    pip install -r requirements.txt
```

- Для создания миграций выполнить команду:

```bash
    python manage.py migrate
```


#### Запуск в контейнерах Docker

- Предварительно необходимо установить Docker для вашей системы.


- Перейти в директорию movies_admin:

```bash
    cd /movies_admin
```

- Создать файл .env по образцу:

```bash
    cp .env.example .env

```
- Перейти в директорию sqlite_to_postgres:

```bash
    cd /sqlite_to_postgres
```

- Создать файл .env по образцу:

```bash
    cp .env.example.docker .env
```


- Находясь в главной директории проекта выполнить команду:


``` bash
    docker-compose up -d --build  
```

