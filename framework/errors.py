from settings import error_pages

error_list = {'404': ('HTTP/1.1 404 Method not found\n\n', '<h1>404<h1>')}


def error(error_numbers):
    headers, body = error_list[error_numbers]

    if str(error_numbers) in error_pages:
        body = error_pages[error_numbers]

    return (headers + body).encode()
