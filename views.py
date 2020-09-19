def home(method, response=False):
    if method == 'GET':
        if response:
            if response == "answer=a2":
                with open('templates/test/yes.html') as template:
                    return template.read()

            else:
                with open('templates/test/no.html') as template:
                    return template.read()

        with open('templates/test/test.html') as template:
            return template.read()
