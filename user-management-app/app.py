from flask import Flask, render_template, request, redirect, url_for
from database import criar_conexao, adicionar_usuario, listar_usuarios, atualizar_usuario, deletar_usuario

app = Flask(__name__)

@app.route('/')
def index():
    usuarios = listar_usuarios()
    return render_template('index.html', usuarios=usuarios)

@app.route('/add', methods=['POST'])
def add_user():
    nome = request.form['nome']
    idade = request.form['idade']
    adicionar_usuario(nome, idade)
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update_user(id):
    nome = request.form['nome']
    idade = request.form['idade']
    atualizar_usuario(id, nome, idade)
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_user(id):
    deletar_usuario(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)