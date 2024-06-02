from flask import Flask ,render_template,request
from main import *
import random


app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')

""" ================================================="""

@app.route('/cadastro')
def home_Pagina():
    
    return render_template('cadastro.html')

@app.route('/salvar', methods=['POST'])
def salvar():
    cpf = request.form['cpf']
    phone = request.form['phone']


    Usuario().insetUser(cpf,phone)

    return 'Cadastro realizado com sucesso'


""" ================================================="""

@app.route('/lista')
def lista():

    listaUsuario = Usuario().queryUser()
    
    return render_template('lista.html',dados = listaUsuario)


@app.route('/ponto')
def point():

    return render_template('pontos.html')

@app.route('/addpoint',methods=['POST'])
def addPoint():

    codic =  request.form['codigo']
    point = request.form['valor']
    point = float(point)

    Ponto().addPonto(codic,point)

    return "Novo Ponto "
@app.route('/query')
def consult():

    return render_template('queryy.html')

@app.route('/consult',methods=['POST'])
def consultaPontos():
    
    user = str(request.form['consulta'])

    codigo = Usuario().queryCpforCode(user)

    return render_template('consulta.html',valor = codigo)

if __name__ == '__main__':
    app.run(port=8080,debug=True)