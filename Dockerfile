# Базовый образ — Python
FROM python:3.11-slim

# Рабочая директория в контейнере
WORKDIR /app

# Копируем все файлы проекта внутрь контейнера
COPY . /app

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Команда для запуска бота
CMD ["python", "bot.py"]
