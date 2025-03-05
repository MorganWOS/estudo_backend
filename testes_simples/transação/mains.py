import json
from http import HTTPStatus, HTTPMethod
import http.server
import socketserver
from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Envie um POST com dados JSON!")

    def do_POST(self):
        # Verifica o tamanho dos dados recebidos
        content_length = int(self.headers['Content-Length'])
        # Lê os dados
        post_data = self.rfile.read(content_length)

        # Converte os dados de JSON para um dicionário Python
        try:
            data = json.loads(post_data)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            # Responde com os dados recebidos
            self.wfile.write(json.dumps(data).encode())
        except json.JSONDecodeError:
            self.send_error(400, "Dados JSON invalidos")

    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()

def run(server_class=HTTPServer, handler_class=MyHandler):
    server_address = ('', 8000)  # Rodando em localhost:8000
    httpd = server_class(server_address, handler_class)
    print("Servidor rodando na porta 8000...")
    httpd.serve_forever()

run()
