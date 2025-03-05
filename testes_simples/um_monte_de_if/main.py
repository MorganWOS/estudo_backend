from usuarios import Usuario as u
from cuidador import Cuidador as c
from tutor import Tutor as t
import screens

print("Sistema de usuario e pagamento!")

rodando = True

users_list = {}

favoritos = []

lista = False

def listarusuario(nome, nick):
    users_list.update({nome: nick})






while rodando:
    escolha = None
    escolha_tc = None

    print("Você deseja se cadastrar ou logar?")
    escolha = int(input("Digite 1 para cadastrar, 2 para logar e 0 para sair do programa: "))

    if escolha == 0:
        rodando = False

    if escolha == 1:
        print("Faça seu cadastro!")
        nome = str(input("Insira seu nome completo: "))
        senha = int(input("Crie uma senha somente com números: "))

        user = u(nome, senha)

        print("Agora nos conte se você deseja ser um cuidador ou se você é um tutor de pet")
        escolha_tc = int(input("Digite 1 para tutor e 2 para cuidador: "))

        if escolha_tc == 1:
            print("Como tutor nos de algumas informações: ")
            nick = str(input("Seu nick-name: "))
            telefone = int(input("Seu telefone: "))
            dt_nascimento = str(input("Sua data de nascimento: "))

            tutor = t(user.nome, user.senha, nick, telefone, dt_nascimento)
            print("Cadastrando...")

            listarusuario(tutor.nome, tutor.nick)

        if escolha_tc == 2:
            print("Para ser um cuidador passe algumas informações: ")
            nick = str(input("Seu nick-name: "))
            telefone = int(input("Seu telefone: "))
            cpf = str(input("Seu cpf: "))

            cuidador = c(user.nome, user.senha, nick, telefone, cpf)
            print("Cadastrando...")

            listarusuario(cuidador.nome, cuidador.nick)

        print(users_list)
        print("Redirecionando para a Home do sistema... \n")

        escolha = screens.telahome()

        while rodando:

            if escolha == 4:
                escolha = screens.telahome()
                if escolha == 1:
                    escolha = screens.telahospedagem()
                    if escolha == 1:
                        escolha = screens.telaAlice()
                        if escolha == 1:
                            escolha = screens.telacontratar()
                            if escolha == 1:
                                print("Cancelado!")
                            elif escolha == 2:
                                print("Serviço contratado!")
                                lista = True
                        elif escolha == 2:
                            favoritos.append("Alice")
                            escolha = screens.telafavoritos(favoritos)
                        elif escolha == 3:
                            print("Denuncia feita!")
            elif escolha == 5:
                escolha = screens.telachat()
            elif escolha == 6:
                escolha = screens.telaserviço(lista)
            if escolha == 7:
                escolha = screens.telaperfil(tutor)
                if escolha == 1:
                    print("Como tutor nos de algumas informações: ")
                    nick = str(input("Seu nick-name: "))
                    telefone = int(input("Seu telefone: "))
                    dt_nascimento = str(input("Sua data de nascimento: "))

                    tutor = t(user.nome, user.senha, nick, telefone, dt_nascimento)
                    print("Cadastrando...")
                    escolha = screens.telaperfil(tutor)

            else:
                rodando = False
                continue
