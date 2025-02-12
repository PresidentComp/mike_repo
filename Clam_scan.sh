#!/bin/bash

# Путь к ClamAV
CLAMAV="/usr/bin/clamscan"

# Путь к директории для сканирования
DIRECTORY="/"

# Email адрес для отчета
REPORT_EMAIL="PresidentComp@gmail.com"

# Проверка существования ClamAV
if ! "$CLAMAV" --version &> /dev/null; then
 echo "ClamAV not found at $CLAMAV"
 exit 1
fi

# Выполнение сканирования без опции --silent, так как она не поддерживается
$CLAMAV --recursive --infected --quiet $DIRECTORY | tee report.txt

# Отправка отчета по электронной почте
echo "New ClamAV Scan Report:" | mail -s "ClamAV Scan Report" $REPORT_EMAIL < report.txt

# Очистка отчета
rm report.txt
