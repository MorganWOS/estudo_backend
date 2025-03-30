"""Quebrado ainda"""
import sqlite3

class BancoDeDados:
    def __init__(self, nome_banco):
        self.conn = sqlite3.connect(nome_banco)
        self.cursor = self.conn.cursor()
        self.criar_tabela()
    
    def criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY,
                nome TEXT,
                preco REAL,
                estoque INTEGER
            )
        """)
        self.conn.commit()
    
    def inserir_produto(self, nome, preco, estoque):
        self.cursor.execute("""
            INSERT INTO produtos (nome, preco, estoque)
            VALUES (?, ?, ?)
        """, (nome, preco, estoque))
        self.conn.commit()
    
    def atualizar_preco(self, id, novo_preco):
        self.cursor.execute("""
            UPDATE produtos SET preco = ?
            WHERE id = ?
        """, (novo_preco, id))
    
    def produtos_em_falta(self):
        self.cursor.execute("SELECT * FROM produtos WHERE estoque <= 0")
        return self.cursor.fetchall()
    
    def fechar_conexao(self):
        self.conn.close()