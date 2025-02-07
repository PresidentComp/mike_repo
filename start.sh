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

echo -e "\033[32m Установка Apache2 завершена.\033[0m"

# Установка Python
sudo apt-get install -y python
python3 --version

echo -e "\033[32m Установка Python завершена.\033[0m"

# Установка и поднятие SSH-сервера
sudo apt-get install ssh
sudo systemctl start ssh
sudo systemctl enable ssh

echo -e "\033[32m Установка SSH завершена.\033[0m"

# Включение PubkeyAuthentication в sshd_config
sudo sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config

# Установка Docker
sudo apt-get install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker

echo -e "\033[32m Установка Docker завершена.\033[0m"

# Установка MySQL-сервера
sudo apt install mysql-server

# Проверка версии MySQL
mysql -V

# Автоматический запуск MySQL при загрузке системы
sudo systemctl start mysql
sudo systemctl enable mysql

echo -e "\033[32m Установка MySQL завершена.\033[0m"

# Установка conky
sudo apt-get install -y conky

# Установка Zenmap (графический интерфейс Nmap)
sudo apt-get install -y zenmap

# Установка Portmaster (мониторинг портов)
sudo apt-get install -y portmaster

echo -e "\033[32m Установка Portmaster завершена.\033[0m"

# Установка Wireshark
sudo apt-get install -y wireshark

echo -e "\033[32m Установка Wereshark завершена.\033[0m"

# Установка FTP
sudo apt-get install vsftpd

# Добавление строк в /etc/vsftpd.conf
sudo sed -i '\$a\ anonymous_enable = NO\n local_enable = YES\n write_enable = YES\n local_umask = 022\n xferlog_enable = YES\n xferlog_std_format=YES\n connect_from_port_20 = YES\n chroot_local_user = YES\n allow_writeable_chroot = YES\n ssl_enable=YES\n ssl_tlsv1=YES\n ssl_sslv2=NO\n ssl_sslv3=NO\n rsa_cert_file=/etc/ssl/private/ssl-cert-snakeoil.pem\n rsa_private_key_file=/etc/sssl_ciphers=HIGH/private/ssl-cert-snakeoil.key\n allow_anon_ssl=NO\n force_local_data_ssl=YES\n force_local_logins_ssl=YES\n ssl_ciphers=HIGH\n use_localtime=YES' /etc/vsftpd.conf

echo -e "\033[32m Установка и настройка FTP завершены.\033[0m"

echo -e "\033[32m Настройка системы завершена.\033[0m"
