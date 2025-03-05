class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def getNome(self):
        print("Retornando nome...")
        return self.nome

    def setNome(self, nome):
        print("Alterando nome...")
        self.nome = nome

    def setSenha(self, senha):
        print("Alterando a senha...")
        self.senha = senha

class Carteira:
    money = 0
    def __init__(self, senha):
        self.senha = senha

    def setSenha(self, senha):
        print("Alterando senha...")
        self.senha = senha

    def depositar(self, dinheiro):
        print(f"Depositando R${dinheiro} na conta...")
        self.money += dinheiro

    def retirar(self, dinheiro):
        print(f"Retirando R${dinheiro} da conta...")
        self.money -= dinheiro

    def getMoney(self):
        print("Printando quantidade de dinheiro na conta...")
        return self.money

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def getNome(self):
        print("Retornando nome...")
        return self.nome

    def getPreco(self):
        print("Retornando preço...")
        return self.preco

    def alterarPreco(valor):
        print(f"Alterando o preço do produto {self.nome}")
        self.preco = valor
