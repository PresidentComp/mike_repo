#!/bin/bash

# Переменные окружения
REPO_BACKPORTS="backports.list"  # Имя файла репозитория
PACKAGES=(apache2 python sshd docker conky zenmap portmaster wireshark)  # Пакеты для установки

# Проверка наличия репозитория Backports и его добавление при необходимости
if ! grep -q "$REPO_BACKPORTS" /etc/apt/sources.list; then
  echo "Добавление репозитория Backports..."
  echo "deb http://packages.linuxmint.com/ backports main" | sudo tee -a /etc/apt/sources.list
  sudo apt-get update
fi

# Обновление пакетного менеджера
sudo apt-get update
sudo apt-get upgrade -y

# Установка необходимых пакетов
for package in "${PACKAGES[@]}"; do
  echo "Установка $package..."
  sudo apt-get install -y $package
done

# Установка и запуск Apache2
sudo apt-get install -y apache2
sudo systemctl start apache2
sudo systemctl enable apache2

# Установка Python
sudo apt-get install -y python

# Установка и поднятие SSH-сервера
sudo apt-get install -y openssh-server
sudo systemctl start ssh
sudo systemctl enable ssh

# Установка Docker
sudo apt-get install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker

# Установка conky
sudo apt-get install -y conky

# Установка Zenmap (графический интерфейс Nmap)
sudo apt-get install -y zenmap

# Установка Portmaster (мониторинг портов)
sudo apt-get install -y portmaster

# Установка Wireshark
sudo apt-get install -y wireshark

echo "Настройка системы завершена."
