import json
import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer
import atexit

# Conecta ao banco de dados
conn = sqlite3.connect('meu_banco.db')
cursor = conn.cursor()

# Cria a tabela (se não existir)
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER
)
''')
conn.commit()

# Fecha a conexão com o banco de dados ao encerrar o servidor
def fechar_conexao():
    conn.close()

atexit.register(fechar_conexao)

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Consulta todos os usuários
        cursor.execute('SELECT * FROM usuarios')
        usuarios = cursor.fetchall()

        # Converte os resultados para JSON
        usuarios_json = json.dumps(usuarios)

        # Envia a resposta
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(usuarios_json.encode())

    def do_POST(self):
        # Lê os dados da requisição
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Converte os dados para um dicionário Python
        try:
            data = json.loads(post_data)
            if isinstance(data, list):  # Verifica se é uma lista
                for usuario in data:
                    nome = usuario.get("nome")
                    idade = usuario.get("idade")
                    if nome and idade:
                        cursor.execute('INSERT INTO usuarios (nome, idade) VALUES (?, ?)', (nome, idade))
                conn.commit()
                self.send_response(201)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"message": "Usuários criados com sucesso"}).encode())
            else:
                self.send_error(400, "Dados JSON inválidos: esperada uma lista de usuários")
        except json.JSONDecodeError:
            self.send_error(400, "Dados JSON inválidos")

def run(server_class=HTTPServer, handler_class=MyHandler):
    server_address = ('0.0.0.0', 8000)
    httpd = server_class(server_address, handler_class)
    print("Servidor rodando na porta 8000...")
    httpd.serve_forever()

run()
