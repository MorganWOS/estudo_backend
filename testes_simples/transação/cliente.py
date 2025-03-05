from usuarios import Usuario, Carteira

print("Crie sua conta de cliente")
nome_cliente = str(input("Seu nome: "))
senha_cliente = str(input("Sua senha: "))
senha_carteira = str(input("Uma senha para sua carteira: "))

client = Usuario(nome_cliente, senha_cliente)
carteira_cliente = Carteira(senha_carteira)
