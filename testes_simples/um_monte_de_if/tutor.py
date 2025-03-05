from usuarios import Usuario

class Tutor(Usuario):
    def __init__(self, nome, senha, nick, telefone, dt_nascimento):
        super().__init__(nome, senha)
        self.nick = nick
        self.telefone = telefone
        self.dt_nascimento = dt_nascimento

        def cadastrar_pet():
            print("Cadastrando pet...")

    
