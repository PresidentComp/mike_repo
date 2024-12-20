import os
import requests
import json
from http.server import HTTPServer, BaseHTTPRequestHandler


# Сканируем сеть
def do_ping_sweep(ip, num_of_host):
    ip_parts = ip.split('.')
    network_ip = ip_parts0 + '.' + ip_parts1 + '.' + ip_parts2 + '.'
    scanned_ip = network_ip + str(int(ip_parts3) + num_of_host)
    response = os.popen(f'ping -c 2 {scanned_ip}').readlines()
    print(f"# Result of scanning: {scanned_ip} #\n{response2.decode().strip()}\n")


# Отправляем HTTP запрос
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


# Обработчик HTTP-запросов
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