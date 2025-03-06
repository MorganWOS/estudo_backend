import requests
import json

url = 'http://172.18.0.2:8000'

def fazerGet():
    print("Enviando GET")
    response = requests.get(url)
    print(f"Resposta do servidor: {response.text}")

def fazerPOST(j):
    print("Fazendo um POST")
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=j, headers=headers)
    print(f"A resposta do servidor foi: {response.json()}")

usuarios = []
rodando = 1
while rodando:
    print("Digite 0 para sair")
    nome = str(input("Digite um nome: "))
    idade = str(input("Digite uma idade: "))
    usuarios.append({"nome": nome, "idade": idade})
    rodando = int(input("Digite 0 (para sair) ou outro número: "))

usuarios_json = json.dumps(usuarios)
print(usuarios_json)
print(usuarios)

fazerPOST(usuarios)
fazerGet()
