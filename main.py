import os
import json
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from datetime import datetime
from jinja2 import Template

# Шлях до директорії storage
STORAGE_DIR = "storage"
DATA_FILE = os.path.join(STORAGE_DIR, "data.json")


# Функція для збереження даних у файл data.json
def save_message(data):
    if not os.path.exists(STORAGE_DIR):
        os.makedirs(STORAGE_DIR)

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            messages = json.load(f)
    else:
        messages = {}

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    messages[timestamp] = data

    with open(DATA_FILE, "w") as f:
        json.dump(messages, f, indent=4)


# Обробник запитів
class MyRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"
        elif self.path == "/read":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.handle_read_request()
            return
        elif self.path == "/error":
            self.path = "/error.html"
        elif self.path.startswith("/storage"):
            self.send_error(404, "Not Found")
            return

        return super().do_GET()

    def do_POST(self):
        if self.path == "/message":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)

            # Парсимо дані форми
            post_data = parse_qs(post_data.decode("utf-8"))
            username = post_data.get("username", [""])[0]
            message = post_data.get("message", [""])[0]

            save_message({"username": username, "message": message})

            self.send_response(302)
            self.send_header("Location", "/")
            self.end_headers()

    def handle_read_request(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                messages = json.load(f)
        else:
            messages = {}

        # Завантажуємо шаблон Jinja2 для відображення повідомлень
        with open("read_template.html", "r") as f:
            template = Template(f.read())

        output = template.render(messages=messages)
        self.wfile.write(output.encode("utf-8"))


def run(server_class=HTTPServer, handler_class=MyRequestHandler, port=3000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
