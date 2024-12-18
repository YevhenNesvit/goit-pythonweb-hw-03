# Використовуємо базовий образ Python
FROM python:3.11

# Копіюємо всі файли в контейнер
COPY . /app

# Перехід до директорії з додатком
WORKDIR /app

# Встановлюємо залежності
RUN pip install jinja2

# Відкриваємо порт 3000
EXPOSE 3000

# Запускаємо сервер
CMD ["python", "main.py"]