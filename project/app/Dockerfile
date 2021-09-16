# образ на основе которого создаём контейнер
FROM python:3.8.6-alpine

# рабочая директория внутри проекта
WORKDIR /usr/src/app

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# переменные окружения для python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# устанавливаем зависимости
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

# копируем содержимое текущей папки в контейнер
COPY . .