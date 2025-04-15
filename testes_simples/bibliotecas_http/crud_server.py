from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sqlite3


class SimpleAPIHandler(BaseHTTPRequestHandler):
    con = sqlite3.connect("testecrud.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE usuario(nickname, nome, dt_nascimento, tipo)")
    cur.close()
    con.close()

    def do_GET(self):
        con = sqlite3.connect("testecrud.db")
        cur = con.cursor()
        if self.path == ('/'):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = cur.execute("SELECT * FROM usuario")
            self.wfile.write(json.dumps(data.fetchall()).encode())
            cur.close()
            con.close()
            return

        self.send_response(400)
        self.end_headers()
        self.wfile.write(json.dumps({'error': 'Task not found'}).encode())
        cur.close()
        con.close()

    def do_POST(self):
        con = sqlite3.connect("testecrud.db")
        cur = con.cursor()
        if self.path == ('/'):
            content_legnth = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_legnth)
            new_data = json.loads(post_data)
            print(new_data)
            cur.execute("INSERT INTO usuario VALUES(?, ?, ?, ?)", (new_data["nick"], new_data["name"], new_data["dt_nascimento"], new_data["tipo"]))
            con.commit()
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message' : 'Usuario adicionado'}).encode())
            cur.close()
            con.close()
            return

        self.send_response(400)
        self.end_headers()
        self.wfile.write(b'Endpoint not found')
        cur.close()
        con.close()


def run():
    server_address = ('', 8050)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print('Servidor rodando em http://localhost:8050')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
