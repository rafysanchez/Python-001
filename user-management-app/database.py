def criar_conexao():
    import sqlite3
    import os

    db_dir = os.path.dirname('exemplo.db')
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir)

    try:
        conexao = sqlite3.connect('exemplo.db')
        return conexao
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def criar_tabela():
    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                            id INTEGER PRIMARY KEY,
                            nome TEXT NOT NULL,
                            idade INTEGER)''')
            conexao.commit()
        except sqlite3.Error as e:
            print(f"Erro ao criar tabela: {e}")
        finally:
            conexao.close()

def adicionar_usuario(nome, idade):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO usuarios (nome, idade) VALUES (?, ?)''', (nome, idade))
    conexao.commit()
    conexao.close()

def listar_usuarios():
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM usuarios ORDER BY id''')
    usuarios = cursor.fetchall()
    conexao.close()
    return usuarios

def atualizar_usuario(id, nome, idade):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute('''UPDATE usuarios SET nome = ?, idade = ? WHERE id = ?''', (nome, idade, id))
    conexao.commit()
    conexao.close()

def deletar_usuario(id):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute('''DELETE FROM usuarios WHERE id = ?''', (id,))
    conexao.commit()
    conexao.close()

# Criar a tabela (se ainda não existir)
criar_tabela()