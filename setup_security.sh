#!/bin/bash

# Функции

# Функция для установки ClamAV
install_clamav() {
    echo "Установка ClamAV..."
    sudo apt-get update
    sudo apt-get install clamav
}

# Функция для установки chkrootkit
install_chkrootkit() {
    echo "Установка chkrootkit..."
    sudo apt-get install chkrootkit
}

# Функция для настройки SELinux
configure_selinux() {
    echo "Настройка SELinux..."
    sudo setenforce 1  # Enforcing SELinux
    sudo semanage fcontext -a -t clamav_var_lib_execpt /var/lib/clamav
    sudo semanage fcontext -a -t clamav_var_log_perm /var/log/clamav
    sudo restorecon -Rv /var/lib/clamav /var/log/clamav
}

# Основная часть скрипта

echo "Инициализация установки и настройки..."

# Установка ClamAV
install_clamav

# Установка chkrootkit
install_chkrootkit

# Настройка SELinux
configure_selinux

echo "Все шаги выполнены успешно!"
