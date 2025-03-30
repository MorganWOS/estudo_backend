"""Quebrado ainda"""
import threading
import time

class Cache:
    def __init__(self, tempo_expiracao):
        self.cache = {}
        self.tempo_expiracao = tempo_expiracao
        self.lock = threading.Lock()
    
    def adicionar(self, chave, valor):
        with self.lock:
            self.cache[chave] = {
                'valor': valor,
                'timestamp': time.time()
            }
    
    def obter(self, chave):
        with self.lock:
            if chave not in self.cache:
                return None
            
            item = self.cache[chave]
            if time.time() - item['timestamp'] > self.tempo_expiracao:
                del self.cache[chave]
                return None
            
            return item['valor']
    
    def limpar_cache(self):
        with self.lock:
            agora = time.time()
            for chave in list(self.cache.keys()):
                if agora - self.cache[chave]['timestamp'] > self.tempo_expiracao:
                    self.cache.pop(chave)

class ServidorCache:
    def __init__(self):
        self.caches = {}
    
    def criar_cache(self, nome, tempo_expiracao):
        if nome in self.caches:
            raise ValueError("Cache já existe")
        self.caches[nome] = Cache(tempo_expiracao)
    
    def obter_cache(self, nome):
        return self.caches.get(nome)
    
    def remover_cache(self, nome):
        if nome in self.caches:
            del self.caches[nome]