import unittest
import sqlite3
from index import criar_conexao, criar_tabela, adicionar_usuario, listar_usuarios, atualizar_usuario, deletar_usuario

class TestUsuarios(unittest.TestCase):
    def setUp(self):
        self.conexao = criar_conexao()
        criar_tabela()

    def test_adicionar_usuario(self):
        adicionar_usuario("Teste", 25)
        
        # Verificar se o usuário foi adicionado
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT nome, idade FROM usuarios WHERE nome=?", ("Teste",))
        resultado = cursor.fetchone()
        conexao.close()
        
        self.assertEqual(resultado[0], "Teste")
        self.assertEqual(resultado[1], 25)

    def test_atualizar_usuario(self):
        # Primeiro adiciona um usuário
        adicionar_usuario("Original", 30)
        
        # Pega o ID do usuário adicionado
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT id FROM usuarios WHERE nome=?", ("Original",))
        id_usuario = cursor.fetchone()[0]
        
        # Atualiza o usuário
        atualizar_usuario(id_usuario, "Atualizado", 35)
        
        # Verifica se foi atualizado
        cursor.execute("SELECT nome, idade FROM usuarios WHERE id=?", (id_usuario,))
        resultado = cursor.fetchone()
        conexao.close()
        
        self.assertEqual(resultado[0], "Atualizado")
        self.assertEqual(resultado[1], 35)

    def test_deletar_usuario(self):
        # Primeiro adiciona um usuário
        adicionar_usuario("Deletar", 40)
        
        # Pega o ID do usuário adicionado
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT id FROM usuarios WHERE nome=?", ("Deletar",))
        id_usuario = cursor.fetchone()[0]
        
        # Deleta o usuário
        deletar_usuario(id_usuario)
        
        # Verifica se foi deletado
        cursor.execute("SELECT * FROM usuarios WHERE id=?", (id_usuario,))
        resultado = cursor.fetchone()
        conexao.close()
        
        self.assertIsNone(resultado)

    def tearDown(self):
        # Limpa a tabela após cada teste
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM usuarios")
        conexao.commit()
        conexao.close()

if __name__ == '__main__':
    unittest.main()