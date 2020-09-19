from framework.sockets import *
from urls import init_urls


def run():
    server_socket = run_and_create_server_socket()

    while True:
        client_socket, request = server_accept(server_socket)
        if not request:
            continue
        method, url = parse_request(request)

        urls = init_urls()
        response = urls.generate_content(url, method)

        send_response_user(client_socket, response)


if __name__ == '__main__':
    run()
