# Web Application with Docker

Цей проект — це простий веб-додаток, створений за допомогою Python та Docker. Він включає маршрутизацію для двох HTML сторінок (`index.html` та `message.html`), обробку форми та збереження повідомлень у файл `data.json`.

## Як побудувати та запустити додаток

### Крок 1: Створення Docker контейнера за допомогою Docker Compose

1. **Перевірте наявність Docker та Docker Compose** на вашому комп'ютері. Якщо Docker ще не встановлено, інсталюйте його, слідуючи [офіційним інструкціям](https://docs.docker.com/get-docker/).

2. **Створіть Docker образ за допомогою Docker Compose**. У терміналі перейдіть до каталогу з проектом та виконайте команду:

   ```bash
   docker-compose up --build