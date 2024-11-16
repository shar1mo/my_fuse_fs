# Используем базовый образ с Python и FUSE
FROM python:3.12-slim

# Устанавливаем необходимые пакеты
RUN apt-get update && apt-get install -y \
    fuse \
    python3-fuse \
    && rm -rf /var/lib/apt/lists/*

# Копируем исходники в контейнер
COPY . /app

# Устанавливаем зависимости
RUN pip install fusepy

# Указываем рабочую директорию
WORKDIR /app

# Команда для запуска скрипта сборки
CMD ["./build_script.sh"]