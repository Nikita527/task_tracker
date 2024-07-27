# Task Management System

Проект для управления задачами с использованием Django, Celery, RabbitMQ, Elasticsearch и Flower. Проект включает создание, чтение, обновление и удаление задач, асинхронную обработку задач с Celery, мониторинг задач с Flower и поиск задач через Elasticsearch.

## Установка и Запуск

### Требования

- Docker
- Docker Compose

### Шаги для запуска

1. Клонируйте репозиторий проекта:
   ```bash
   git clone <URL вашего репозитория>
   cd <название директории проекта>

2. Содать файл .env согласно .env.enxample

3. Запуск и сборка контейнеров Docker:
    cd infra
    docker-compose up -d

4. Загрузить тестовые данные можно из контейнера tasks_backend
    docker-compose exec task_tracker-backend python load_test_data.py

5. Примеры API запросов:
    API для управления задачами доступно по адресу http://localhost:8000/api/tasks/

    Создание задачи:
        curl -X POST "http://localhost:8000/api/tasks/" -H "Content-Type: application/json" -d '{
            "name": "Новая задача",
            "description": "Описание новой задачи",
            "status": "queued"
        }'

    Обновление задачи (указать ID задачи, например, 1):
        curl -X PUT "http://localhost:8000/api/tasks/1/" -H "Content-Type: application/json" -d '{
            "name": "Обновленная задача",
            "description": "Обновленное описание задачи",
            "status": "in_progress"
        }'

    Удаление задачи (указать ID задачи, например, 1):
        curl -X DELETE "http://localhost:8000/api/tasks/1/"

    Получение списка задач:
        curl -X GET "http://localhost:8000/api/tasks/"

    Поиск задач через Elasticsearch:
        curl -X GET "http://localhost:8000/api/tasks/search/?q=Новая+задача"

    Демонстрация работы Flower:
        Flower для мониторинга Celery задач доступен по адресу http://localhost:5555.
