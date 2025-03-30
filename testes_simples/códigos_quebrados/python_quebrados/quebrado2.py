"""Quebrado ainda"""
class GerenciadorUsuarios:
    def __init__(self):
        self.usuarios = []
    
    def adicionar_usuario(self, nome, idade):
        self.usuarios.append({'nome': nome, 'idade': idade})
    
    def remover_usuario(self, nome):
        for usuario in self.usuarios:
            if usuario['nome'] == nome:
                self.usuarios.remove(usuario)
    
    def usuario_mais_velho(self):
        mais_velho = None
        for usuario in self.usuarios:
            if mais_velho is None or usuario['idade'] > mais_velho['idade']:
                mais_velho = usuario
        return mais_velho['nome']
    
    def media_idades(self):
        total = 0
        for usuario in self.usuarios:
            total += usuario['idade']
        return total / len(self.usuarios)