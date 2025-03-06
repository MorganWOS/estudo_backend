import sqlite3

# Conecta ao banco de dados (ou cria se não existir)
conn = sqlite3.connect('meu_banco.db')
cursor = conn.cursor()

# Cria a tabela (se não existir)
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER
)
''')

# Insere alguns usuários
cursor.execute('INSERT INTO usuarios (nome, idade) VALUES ("Joao", 30)')
cursor.execute('INSERT INTO usuarios (nome, idade) VALUES ("Maria", 25)')

# Salva as alterações
conn.commit()

# Consulta todos os usuários
cursor.execute('SELECT * FROM usuarios')
usuarios = cursor.fetchall()

# Exibe os resultados
print("Usuários:")
for usuario in usuarios:
    print(usuario)

# Fecha a conexão
conn.close()
