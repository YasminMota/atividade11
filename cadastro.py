from PyQt5 import uic,QtWidgets 
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_conta"
)

def funcao_principal(): 
    campo1 = formulario.lineEdit.text() 
    campo2 = formulario.lineEdit_2.text()
    campo3 = formulario.lineEdit_3.text()
    campo4 = formulario.lineEdit_4.text()
    
    print("----- DADOS ------------------")

    sexo = " "

    if formulario.radioButton.isChecked(): 
        print("Sexo : Feminino")
        sexo = "Feminino"
    else:
        print("Sexo : Masculino")
        sexo = "Masculino"


    print("Nome:", campo1)
    print("Sobrenome:", campo2)
    print("Email:", campo3)
    print("Idade:", campo4)

    cursor = banco.cursor()
    comando = "INSERT INTO cadastro (nome,sobrenome,email,idade,sexo) VALUES (%s,%s,%s,%s,%s)"
    dados = (str(campo1),str(campo2),str(campo3),str(campo4),sexo)
    cursor.execute(comando,dados)
    banco.commit()



app=QtWidgets.QApplication([])   
formulario=uic.loadUi("formulario.ui") 
formulario.pushButton.clicked.connect(funcao_principal)  

formulario.show()
app.exec()



