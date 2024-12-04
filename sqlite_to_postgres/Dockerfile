# Dockerfile

FROM python:3.12-slim

# Установка зависимостей
WORKDIR /sqlite_to_postgres

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода
COPY . .

# Команда для запуска приложения
CMD ["python", "main.py"]