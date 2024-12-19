import os
import argparse
import requests
import json
# coding=utf-8
from http.server import HTTPServer, BaseHTTPRequestHandler

# Обработка запросов
class ServiceHandler(BaseHTTPRequestHandler):
    # Устанавливаем параметры заголовков для ответа
    def set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        length = int(self.headers["Content-Length"])
        content = self.rfile.read(length)
        temp = str(content).strip('b\'')
        self.end_headers()
        return temp

    # Сканируем сеть
    def do_ping_sweep(ip, num_of_host):
        ip_parts = ip.split('.')
        network_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'
        scanned_ip = network_ip + str(int(ip_parts[3]) + num_of_host)
        response = os.popen(f'ping -c 2 {scanned_ip}').readlines()
        print(f"[#] Result of scanning: {scanned_ip} [#]\n{response[2]}\n", end='')

    # Отправляем HTTP запрос
    def sent_http_request(target, method, headers=None, payload=None):
        #  Формируем словарь для HTTP-заголовков
        headers_dict = {}
        if headers:
            for header in headers:
                header_name = header.split(":")[0]
                header_value = header.split(":")[1:]
                headers_dict[header_name] = ":".join(header_value)
        # Если пользователь выбрал метод GET
        if method == "GET":
            # Проверяем возможность подключения к ресурсу
            try:
                response = requests.get(target, headers=headers_dict, timeout=10)
            # Если такой ресурс существует, но не отвечает
            except requests.exceptions.Timeout:
                print(f"Время ожидания ответа {target} вышло")
                return
            # Во всех остальных случаях предполагаем, что пользователь ввёл неверный адрес
            except:
                print(f"Неверный адрес ресурса {target}")
                return
        # Если пользователь выбрал метод POST
        elif method == "POST":
            # Проверяем возможность подключения к ресурсу
            try:
                response = requests.post(target, headers=headers_dict, data=payload, timeout=10)
            # Если такой ресурс существует, но не отвечает
            except requests.exceptions.Timeout:
                print(f"Время ожидания ответа {target} вышло")
                return
            # Во всех остальных случаях предполагаем, что пользователь ввёл неверный адрес
            except:
                print(f"Неверный адрес ресурса {target}")
                return
        # Если пользователь забыл указать метод, то сообщаем ему об этом
        else:
            print(f"Не выбран метод GET или POST для ресурса {target}")
            return
        # Выводим ответ
        print(
            f"[#] Код ответа: {response.status_code}\n"
            f"[#] Заголовок ответа: {json.dumps(dict(response.headers), indent=4, sort_keys=True)}\n"
            f"[#] Телоо ответа:\n {response.text}"
        )
        # Закрываем подключение, если оно случилось
        response.close()

    # Работаем со скриптом из терминала
    parser = argparse.ArgumentParser(description='Network scanner')
    parser.add_argument('task', choices=['scan', 'sendhttp'], help='Network scan or send HTTP request')
    parser.add_argument('-i', '--ip', type=str, help='IP address')
    parser.add_argument('-n', '--num_of_hosts', type=int, help='Number of hosts')
    parser.add_argument('-t', '--target', type=str, help='URL')
    parser.add_argument('-m', '--method', type=str, help='Method')
    parser.add_argument('-hd', '--headers', type=str, nargs='*', help='Headers')
    args = parser.parse_args()

    if args.task == 'scan':
        if not args.ip or not args.num_of_hosts:
            print("Error: Missing required arguments '-i IP' and '-n NUM_OF_HOSTS' for network scan.")
        else:
            for host_num in range(args.num_of_hosts):
                do_ping_sweep(args.ip, host_num)
    elif args.task == 'sendhttp':
        if not args.target or not args.method:
            print("Error: Missing required arguments '-t TARGET' and '-m METHOD' for HTTP request.")
        elif not args.headers or args.headers == '':
            print("Error: Missing or empty headers argument '-hd HEADERS'.")
        else:
            sent_http_request(args.target, args.method, args.headers)
    else:
        print("Error: Invalid choice for argument 'task'.")

# Запускаем HTTP сервер
server = HTTPServer(('0.0.0.0', 8082), ServiceHandler)
server.serve_forever()