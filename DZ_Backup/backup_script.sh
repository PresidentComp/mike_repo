#!/bin/bash

# Определяем директории для резервного копирования
BACKUP_DIR="/backup"
LOG_DIR="/var/log"
HOME_DIR="/home"
SSH_CONFIG_FILE="/etc/ssh/sshd_config"
RDP_CONFIG_FILE="/etc/xrdp/xrdp.ini"
FTP_CONFIG_FILE="/etc/vsftpd.conf"

# Проверяем наличие директории для резервного копирования
if [ ! -d "$BACKUP_DIR" ]; then
    mkdir -p "$BACKUP_DIR"
    echo "Создана директория для резервного копирования: $BACKUP_DIR"
fi

# Копируем файлы конфигурации SSH
cp "$SSH_CONFIG_FILE" "$BACKUP_DIR/ssh_config.bak"

# Копируем файлы конфигурации RDP
cp "$RDP_CONFIG_FILE" "$BACKUP_DIR/xrdp.ini.bak"

# Копируем файлы конфигурации FTP (если есть)
cp "$FTP_CONFIG_FILE" "$BACKUP_DIR/vsftpd.conf.bak"

# Копируем директорию /home
cp -r "$HOME_DIR" "$BACKUP_DIR/home_backup"

# Копируем директорию /var/log
cp -r "$LOG_DIR" "$BACKUP_DIR/log_backup"

# Создаём архив с резервными копиями
tar -czvf "$BACKUP_DIR/system_backup.tar.gz" "$BACKUP_DIR"/{home_backup,log_backup,ssh_config.bak,xrdp.ini.bak,vsftpd.conf.bak}

# Удаляем старые резервные копии (если нужно)
find "$BACKUP_DIR" -type f -name "*.tar.gz" -mtime +7 -exec rm -f {} \;

echo "Резервное копирование завершено."
