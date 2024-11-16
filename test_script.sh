#!/bin/bash

# Тестирование создания каталога
mkdir /mnt/fuse_mount/test_dir
if [ -d "/mnt/fuse_mount/test_dir" ]; then
    echo "Тест создания каталога пройден"
else
    echo "Тест создания каталога не пройден"
    exit 1
fi

# Тестирование создания файла
echo "Hello, FUSE!" > /mnt/fuse_mount/test_file.txt
if [ -f "/mnt/fuse_mount/test_file.txt" ]; then
    echo "Тест создания файла пройден"
else
    echo "Тест создания файла не пройден"
    exit 1
fi

# Тестирование чтения файла
content=$(cat /mnt/fuse_mount/test_file.txt)
if [ "$content" == "Hello, FUSE!" ]; then
    echo "Тест чтения файла пройден"
else
    echo "Тест чтения файла не пройден"
    exit 1
fi

# Тестирование удаления файла
rm /mnt/fuse_mount/test_file.txt
if [ ! -f "/mnt/fuse_mount/test_file.txt" ]; then
    echo "Тест удаления файла пройден"
else
    echo "Тест удаления файла не пройден"
    exit 1
fi

# Тестирование удаления каталога
rmdir /mnt/fuse_mount/test_dir
if [ ! -d "/mnt/fuse_mount/test_dir" ]; then
    echo "Тест удаления каталога пройден"
else
    echo "Тест удаления каталога не пройден"
    exit 1
fi

echo "Все тесты пройдены успешно"