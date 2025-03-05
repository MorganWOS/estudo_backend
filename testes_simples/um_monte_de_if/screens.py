def telahome():
    print("-------HOME--------")
    print("\n Como esta o seu dia?")
    print("\n \n1-Hospedagem")
    print("Passeio")
    print("Pet Sitter")
    print("\n \n Escolha uma dessas opções ou troque para outra tela.")
    print("4-Home  5-Chat  6-Serviço  7-Perfil")
    escolha = int(input("Escolha a tela: "))
    return escolha

def telachat():
    print("-------CHAT--------")
    print("\n Com quem deseja conversar?")
    print("\n \n1-Bot1 :)")
    print("Bot2 UwU")
    print("Bot3 OwO")
    print("\n\n")
    print("4-Home  5-Chat  6-Serviço  7-Perfil")
    escolha = int(input("Escolha um opção: "))
    return escolha

def telaserviço(lista):
    if lista:
        print("-------CHAT--------")
        print("\nSeus serviços passados: ")
        print("\n\nAlguns serviços....")
        print("Alice(Hospedagem)")
        print("\n\n")
        print("4-Home  5-Chat  6-Serviço  7-Perfil")
        escolha = int(input("Escolha um opção: "))
        return escolha
    print("-------CHAT--------")
    print("\nSeus serviços passados: ")
    print("\n\nAlguns serviços....")
    print("\n\n")
    print("4-Home  5-Chat  6-Serviço  7-Perfil")
    escolha = int(input("Escolha um opção: "))
    return escolha

def telaperfil(user):
    print("-------CHAT--------")
    print("\nAqui esta suas informações:")
    print("\n\n")
    print(f"Nome: {user.nome}")
    print(f"Nick: {user.nick}")
    print(f"Data de Nascimento: {user.dt_nascimento}")
    print(f"Telefone: {user.telefone}")
    print("\n\n")
    print("Digite 1 para alterar os dados")
    print("4-Home  5-Chat  6-Serviço  7-Perfil")
    escolha = int(input("Escolha um opção: "))
    return escolha

def telahomecuidador():
    print("-------HOME--------")
    print("\n Como esta o seu dia?")
    print("\n\n1-Criar serviço")
    print("2-Alterar serviço")
    print("4-Home  5-Chat  6-Serviço  7-Perfil")
    escolha = int(input("Escolha a tela: "))
    return escolha

def telahospedagem():
    print("-------Hospedagens--------")
    print("\n Como esta o seu dia?")
    print("1-Alice(Hospedagem R$20.0 por noite)")
    print("Jeferson(Hospedagem R$40.0 por noite)")
    print("Golias(Hospedagem R$30.0 por noite)")
    print("Jessica(Hospedagem R$60.0 por noite)")
    print("4-Home  5-Chat  6-Serviço  7-Perfil")
    escolha = int(input("Escolha a tela: "))
    return escolha

def telaAlice():
    print("-------Alice--------")
    print("\nDescrição: Adoro cachorros e posso cuidar muito bem do seu pet bla bla bla...")
    print("\n\n1-Contratar")
    print("2-Favoritar")
    print("3-Denunciar")
    print("\n4-Home  5-Chat  6-Serviço  7-Perfil")
    escolha = int(input("Escolha a tela: "))
    return escolha

def telacontratar():
    print("-------Alice--------")
    print("\nContrato")
    print("1-Cancelar")
    print("2-Pagar")
    print("\n4-Home  5-Chat  6-Serviço  7-Perfil")
    escolha = int(input("Escolha a tela: "))
    return escolha

def telafavoritos(lista):
    print("-------Favoritos--------\n\n")
    print(lista)
    print("\n4-Home  5-Chat  6-Serviço  7-Perfil")
    escolha = int(input("Escolha a tela: "))
    return escolha
