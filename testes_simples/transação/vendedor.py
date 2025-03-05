"""Um teste de transação simples!"""
from usuarios import Usuario, Produto, Carteira

rodando = True

while rodando:
    print("Crie sua conta de vendedor")
    nome = str(input("Qual seu nome completo: "))
    senha = str(input("Agora crie sua senha: "))
    vendedor = Usuario(nome, senha)
    print("1-Printa o nome")
    print("2-Altera o nome")
    print("3-Altera a senha")
    escolha = int(input("Escolha uma das opções: "))
    if escolha == 1:
        print(vendedor.getNome())
    if escolha ==2:
        nome = str(input("Altere seu nome: "))
        vendedor.setNome(nome)
        print(vendedor.getNome())
    if escolha == 3:
        senha = str(inpu("Altere sua senha: "))
        vendedor.setSenha()
    senha_carteira = str(input("Crie uma senha para sua carteira: "))
    carteira_vendedor = Carteira(senha)
    print("Crie seus produtos -->")
    criando = True
    produtos = {}
    while criando:
        nome_produto = str(input("Nome do produto: "))
        preco_produto = float(input("Preço do produto: R$"))
        produtos[nome_produto] = preco_produto
        criando = int(input("Digite 0 para sair: "))
    comprando = True
    while comprando:
        print("Compre os produtos -->")
        print(produtos)
        compra = str(input("Digite o nome do produto que deseja comprar: "))
        carteira_vendedor.depositar(produtos[compra])
        comprando = int(input("Digite 0 para sair: "))
    print(carteira_vendedor.getMoney())
    rodando = False
