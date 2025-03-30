from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleAPIHandler(BaseHTTPRequestHandler):
    #Uma persistencia simples de dados na memoria, simulando um banco de dados
    db = {
        'tasks': [
            {'id': 1, 'task': 'Tarefa 1'},
            {'id': 2, 'task': 'Tarefa 2'},
            {'id': 3, 'task': 'Tarefa 3'}
        ]
    }

    def do_GET(self):
        path_parts = self.path.split('/') #Separa o path em partes com 'split' entre as '/'
    
        if len(path_parts) == 3 and path_parts[1] == 'tasks' and path_parts[-1].isdigit(): #Verifica as condições necessarias para um busca por id com 3 partes
            task_id = int(path_parts[-1])
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            for task in self.db['tasks']: #Percorre as tasks e pega a task com o mesmo id da busca
                if task['id'] == task_id:
                    self.wfile.write(json.dumps(task).encode())
                    return  
            

            self.send_response(404)
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Task not found'}).encode())

        if self.path == '/tasks': #Verifica se é o caminho certo
            print(self.path.split('/'))
            self.send_response(200)
            self.send_header('Content-type', 'application/json') #Define o tipo de conteudo
            self.end_headers()
            self.wfile.write(json.dumps(self.db['tasks']).encode())
            #Retorna 200 e o conteudo do 'banco de dados'
        else:
            # Se não for o camiho certo retorna o erro 404
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Endpoint not found')


    def do_POST(self):
        if self.path == '/tasks':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length) #Lê o conteudo do POST em bytes
            
            new_task = json.loads(post_data) #Converte o conteudo para um dicionario
            new_task['id'] = len(self.db['tasks']) + 1 #Adiciona um id novo incremental
            self.db['tasks'].append(new_task) #Adiciona a nova tarefa ao banco de dados
            
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(new_task).encode()) #Retorna 201 e a nova tarefa em bytes
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Endpoint not found')

    def do_PUT(self):
        if self.path == '/tasks':
            content_lenght = int(self.headers['Content-Length'])
            put_data = self.rfile.read(content_lenght)
            update_task = json.loads(put_data) #Converte o conteudo para um dicionario
            task_id = update_task['id'] #Pega o id da tarefa atualizada
            for task in self.db['tasks']: #Percorre as taskk, identifica e atualiza a task que tem o id igual ao da nova tarefa
                if task['id'] == task_id:
                    task.update(update_task)
                    break
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(update_task).encode())

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Task not found')
            return
    
    def do_DELETE(self):
        if self.path == '/tasks':
            content_legnth = int(self.headers['Content-Length'])
            dado_deletavel = self.rfile.read(content_legnth)
            task_id = json.loads(dado_deletavel)['id'] #Converte o conteudo para um dicionario e pega o id da task
            for task in self.db['tasks']: #Percorre as tasks e identifica qual deve ser deletada
                if task['id'] == task_id:
                    self.db['tasks'].remove(task)
                    break
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Task deleted'}).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Task not found')


def run():
    server_address = ('', 8050)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print('Servidor rodando em http://localhost:8050')
    httpd.serve_forever()

if __name__ == '__main__':
    run()