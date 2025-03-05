from usuarios import Usuario

class Cuidador(Usuario):
    def __init__(self, nome, senha, nick, telefone, cpf):
        super().__init__(nome, senha)
        self.nick = nick
        self.telefone = telefone
        self.cpf = cpf


    def criar_serviço():
        print("Criando serviço...")

    def apagar_serviço():
        print("Deletando serviço...")
