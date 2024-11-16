#!/bin/bash

# Создаем директорию для монтирования
mkdir -p /mnt/fuse_mount

# Запускаем скрипт для монтирования файловой системы
python3 my_fuse_fs.py /mnt/fuse_mount