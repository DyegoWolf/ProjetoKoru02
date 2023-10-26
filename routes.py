from flask import Flask, render_template, request, redirect, url_for
import repositorio

app = Flask(__name__)

# Definição de uma rota
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/equipe")
def equipe():
    dicionario = repositorio.retornar_membros()
    return render_template("crud_equipe.html", dados=dicionario)

@app.route("/novo_membro")
def novo_membro():
    return render_template("cadastro.html")

@app.route("/equipe/<int:id>", methods=['GET', 'POST'])
def editar_membro(id):

    #Usuário está mandando dados
    if request.method == "POST":

        #Verifica se o botão Excluir foi pressionado pelo usuário
        if "excluir" in request.form:
            repositorio.remover_membro(id)
            return redirect(url_for('index'))
        
        #Verifica se o botão Salvar foi pressionado pelo usuário
        elif "salvar" in request.form:
            membro = {}
            membro['nome'] = request.form['nome']
            membro['descricao'] = request.form['descricao']
            membro['foto'] = request.form['foto']

            #Verifica se a chave existe e se sim, atualiza os campos do membro
            if id in repositorio.retornar_membros().keys():
                repositorio.atualizar_membro(id, membro)

            return redirect(url_for('index'))

    #Usuário está esperando dados
    elif request.method == "GET":
        
        #Retorna os dados de um membro na página de cadastro
        membro = repositorio.retornar_membro(id)
        membro['id'] = id
        return render_template("cadastro.html", **membro)


@app.route("/membro", methods=["GET", "POST"])
def criar_membro():
    if request.method == "POST":
        membro = {}
        membro['nome'] = request.form['nome']
        membro['descricao'] = request.form['descricao']
        membro['foto'] = request.form['foto']
        repositorio.criar_membro(**membro)
        return redirect(url_for('index')) 

    elif request.method == "GET":
        return render_template("cadastro.html", id=repositorio.gerar_id())

app.run(debug=True)