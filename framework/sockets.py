import socket
from settings import *


def run_and_create_server_socket():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, int(not freeze_after_shutdown))
    server_socket.bind((address, port))
    server_socket.listen()

    return server_socket


def server_accept(server_socket):
    client_socket, addr = server_socket.accept()
    request = client_socket.recv(1024)

    return client_socket, request.decode('utf-8')


def parse_request(request):
    parsed = request.split(' ')
    method = parsed[0]
    print(parsed)
    url = parsed[1]

    return method, url


def send_response_user(client_socket, response):
    client_socket.sendall(response)
    client_socket.close()