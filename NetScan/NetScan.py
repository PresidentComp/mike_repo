import os
import requests
import json
from http.server import HTTPServer, BaseHTTPRequestHandler


# Сканируем сеть
# def do_ping_sweep(ip, num_of_host): - Объявление функции с двумя параметрами: ip и num_of_host.
# ip_parts = ip.split('.') - Разбиение IP-адреса на части, используя точку в качестве разделителя.
# Результатом будет список частей IP-адреса.
# network_ip = ip_parts0 + '.' + ip_parts1 + '.' + ip_parts2 + '.'
# - Формирование сетевой части IP-адреса путем объединения первых трех частей IP-адреса.
# scanned_ip = network_ip + str(int(ip_parts3) + num_of_host)
# - Создание сканируемого IP-адреса путем добавления значения num_of_host к последней части IP-адреса.
# response = os.popen(f'ping -c 2 {scanned_ip}').readlines()
# - Выполнение команды ping с параметрами -c 2, что означает отправку двух пакетов ICMP ECHO_REQUEST.
# Результат выполнения команды сохраняется в переменной response.
# print(f"# Result of scanning: {scanned_ip} #\n{response2.decode().strip()}\n")
# - Вывод результата сканирования.
def do_ping_sweep(ip, num_of_host):
    ip_parts = ip.split('.')
    network_ip = ip_parts0 + '.' + ip_parts1 + '.' + ip_parts2 + '.'
    scanned_ip = network_ip + str(int(ip_parts3) + num_of_host)
    response = os.popen(f'ping -c 2 {scanned_ip}').readlines()
    print(f"# Result of scanning: {scanned_ip} #\n{response2.decode().strip()}\n")


# Отправляем HTTP запрос
# def sent_http_request(target, method, headers=None, payload=None):
# - Объявление функции, которая принимает следующие параметры:
# target: URL ресурса, к которому отправляется запрос.
# method: метод запроса (GET или POST).
# headers: словарь заголовков.
# payload: данные для отправки в теле POST-запроса.
# headers_dict = {}
# - Инициализация пустого словаря для хранения заголовков.
# if headers:
# - Проверка наличия заголовков. Если заголовки переданы, выполняется следующий блок кода.
# for header in headers:
# - Перебор всех заголовков, переданных в параметре headers.
# header_name, header_value = header.split(':')
# - Разделение каждого заголовка на имя и значение.
# headers_dict[header_name.strip()] = header_value.strip()
# - Добавление заголовка в словарь headers_dict.
# if method == "GET":
# - Проверка, является ли метод запроса GET. Если да, выполняется следующий блок кода.
# try:
# - Начало блока try, в котором выполняется запрос GET.
# response = requests.get(target, headers=headers_dict, timeout=10)
# - Выполнение GET-запроса к указанному URL с переданными заголовками и таймаутом 10 секунд.
# except requests.exceptions.Timeout:
# - Обработка исключения таймаута. Если время ожидания ответа истекло, выводится соответствующее сообщение.
# except Exception as e:
# - Обработка всех остальных исключений. Если возникает ошибка, выводится сообщение с указанием причины.
# elif method == "POST":
# - Проверка, является ли метод запроса POST. Если да, выполняется следующий блок кода.
# response = requests.post(target, headers=headers_dict, data=payload, timeout=10)
# - Выполнение POST-запроса к указанному URL с переданными заголовками, данными и таймаутом 10 секунд.
# except requests.exceptions.Timeout:
# - Обработка исключения таймаута для POST-запроса.
# except Exception as e:
# - Обработка всех остальных исключений для POST-запроса.
# else:
# - Если метод запроса не был ни GET, ни POST, выводится сообщение об ошибке
def sent_http_request(target, method, headers=None, payload=None):
    headers_dict = {}
    if headers:
        for header in headers:
            header_name, header_value = header.split(':')
    headers_dictheader_name.strip() = header_value.strip()

    if method == "GET":
        try:
            response = requests.get(target, headers=headers_dict, timeout=10)
    print(
        f"# Код ответа: {response.status_code}\n"
        f"# Заголовок ответа: {json.dumps(dict(response.headers), indent=4, sort_keys=True)}\n"
        f"# Тело ответа:\n {response.text}"
    )
    except requests.exceptions.Timeout:
    print(f"Время ожидания ответа {target} вышло")
    except Exception as e:
    print(f"Неверный адрес ресурса {target}: {e}")
    elif method == "POST":
    try:
        response = requests.post(target, headers=headers_dict, data=payload, timeout=10)
    print(
        f"# Код ответа: {response.status_code}\n"
        f"# Заголовок ответа: {json.dumps(dict(response.headers), indent=4, sort_keys=True)}\n"
        f"# Тело ответа:\n {response.text}"
    )
    except requests.exceptions.Timeout:
    print(f"Время ожидания ответа {target} вышло")
    except Exception as e:
    print(f"Неверный адрес ресурса {target}: {e}")
    else:
    print(f"Не выбран метод GET или POST для ресурса {target}")

class ServiceHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

    self.send_header('Content-type', 'text/json')
    self.end_headers()
    self.wfile.write(json.dumps({"result": "OK"}).encode())

    def do_POST(self):
        self.send_response(200)

    self.send_header('Content-type', 'text/json')
    self.end_headers()
    content_length = int(self.headers['Content-Length'])
    content = self.rfile.read(content_length).decode()
    self.wfile.write(json.dumps({"result": "POST request received"}).encode())

    def do_ping(self):
        self.send_response(200)

    self.send_header('Content-type', 'text/json')
    self.end_headers()
    content = self.rfile.read(int(self.headers['Content-Length'])).decode()
    self.wfile.write(json.dumps({"result": do_ping_sweep(content)}).encode())


# Запускаем HTTP сервер
server = HTTPServer(('0.0.0.0', 8082), ServiceHandler)
server.serve_forever()