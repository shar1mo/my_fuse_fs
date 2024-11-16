# Виртуальная файловая система в памяти с использованием FUSE

## Установка и запуск

1. Склонируйте репозиторий:

    ```bash
    git clone https://github.com/shar1mo/my_fuse_fs.git
    cd my_fuse_fs
    ```

2. Соберите и запустите контейнер:

    ```bash
    docker build -t my_fuse_fs .
    docker run -it --privileged my_fuse_fs
    ```

3. Выполните автоматическое тестирование:

    ```bash
    docker run -it --privileged my_fuse_fs ./test_script.sh
    ```

## Ручной запуск

1. Активируйте виртуальное окружение:

    ```bash
    source my_fuse_env/bin/activate
    ```

2. Запустите скрипт для монтирования файловой системы:

    ```bash
    python3 my_fuse_fs.py /mnt/fuse_mount
    ```

3. Выполните операции с файловой системой:

    ```bash
    cd /mnt/fuse_mount
    mkdir test_dir
    echo "Hello, FUSE!" > test_file.txt
    cat test_file.txt
    rm test_file.txt
    rmdir test_dir
    ```

4. Размонтируйте файловую систему:

    ```bash
    fusermount -u /mnt/fuse_mount
    ```

## Зависимости

- Python 3.12
- fusepy
- FUSE
## Установка необходимых пакетов
1. Размонтируйте файловую систему:

   sudo apt update
   sudo apt install python3-venv
## Создание виртуального окружения
1. Размонтируйте файловую систему:

   mkdir ~/my_fuse_env
   cd ~/my_fuse_env
   python3 -m venv my_fuse_env
## Активация виртуального окружения

   source my_fuse_env/bin/activate
## Установка пакетов в виртуальное окружение
    pip install fusepy
## Использование виртуального окружения
    python3 ~/my_fuse_fs/my_fuse_fs.py

## Создание файлов и каталогов
    cd ~/my_fuse_fs_mount
    
    Создать каталог:
    mkdir test_dir
    Создай файл:
    touch test_file.txt
## Удаление файлов и каталогов
    rm test_file.txt
    rmdir test_dir
## Запись данных в файл
    echo "Hello, FUSE!" > test_file.txt
    echo "More data" >> test_file.txt //v konew file
## Проверка работы файловой системы
    cat test_file.txt
    ls