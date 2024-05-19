import sqlite3
import os,sys

# CADASTRO DE USUARIO AO BANCO DE DADOS

    # CPF
    # CELULAR
    # CODIGO

# USUARIO INFORMACAO

    # CPF
    # CODIGO
    # CELULAR
    # PONTOS

# PONTOS

    # ADD PONTOS
    # CONSULTAR PONTOS

# ADMIN

    # BACKUP
    # EXCLUIR USUARIO
    # EXCLUIR BANCO DE DADOS


class Usuario():

    def __init__(self):
    
        self.conn = sqlite3.connect('user.db')
        self.c = self.conn.cursor()

        logg = (f'Banco: {self.conn} CONECTADO')

        print(logg)
        
    def creatTablet(self):
        self.c.execute(""" 
        CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        cpf TEXT NOT NULL,celular TEXT NOT NULL,
        codigo TEXT NOT NULL,ponto INTEGER NOT NULL) 
        """)
        self.conn.commit()

        print('TABELA CONECTADO usuarios')

    def insetUser(self,cpf,celular,codigo,ponto=0):

        self.cpf = cpf
        self.celular = celular
        self.codigo = codigo
        self.ponto = ponto

        self.c.execute("INSERT INTO usuarios (cpf,celular,codigo,ponto)VALUES(?,?,?,?)", (self.cpf,self.celular,self.codigo,self.ponto))

        self.conn.commit()

        print('Novo Usuario Criado com Sucesso!')


    def queryPoint(self,codigo):

        self.codigo = codigo
        consulta = self.c.execute("SELECT * FROM usuarios")

        for i in consulta:
            if self.codigo in i:
                print('-------------------------------------------')
                print(i)

    def queryUser(self):

        consulta = self.c.execute("SELECT * FROM usuarios")
        for i in consulta:
            print("\n" ,i)

    def queryCpforCode(self,cpf_codigo):

        consul = self.c.execute('SELECT * FROM usuarios')
        for i in consul:            
            cpf = (i[1])
            codigo = (i[3])

            if cpf_codigo == cpf or cpf_codigo == codigo:
                print(i)
                    
# SISTEMA DE PONTOS
            
class Ponto(Usuario):

    def addPonto(self,codigo,valor):

        # COLETA O VALOR ANTES DE ATUALIZAR PARA SOMAR OS PONTO

        dados = self.c.execute("SELECT * FROM usuarios")

        for i in dados:
            if codigo in i:
                saldo = int(i[4])

        if valor < 50 :
                ponto = + 5
        elif valor < 100 : 
            ponto = +10
        elif valor < 150 :
            ponto = +15
        elif valor < 250 :
            ponto =+ 20

        elif valor < 350:
            ponto =+ 30

        elif valor > 350 :
            ponto =+ 50

            
        ponto = ponto + saldo

        self.c.execute(f"UPDATE usuarios SET ponto = {ponto} WHERE codigo ={codigo}")
        self.conn.commit()
        print('Ponto Add Com Sucesso!')

"""

if __name__ == "__main__":
    Usuario().creatTablet()
     
"""




# ADD USUARIO
# Usuario().insetUser('000999777','73999249926','1020')
# ADD PONTO AO ABASTECER
#Ponto().addPonto('1001',300)


# CONSULTA PONTO 
#Usuario().queryCpforCode('2002')


# ADMINISTRACAO SYSTEMA

class Admin():

    def pasta(self):
        dados = os.listdir()

        for arquivo in dados:
            if ".db" in arquivo :
                arquivo = str(arquivo)
                print(arquivo)

                os.renames(arquivo,'backup/dados.db')
