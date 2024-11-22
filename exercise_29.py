# PyQt5 Line edits

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QWidget, QPushButton

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()      #Se usa super() para poder acceder al constructor de la clase padre y a sus atributos y metodos.
        self.setGeometry(700, 300, 500, 500)  #El metodo setGeometry(x,y,width,height) nos permite modificar la posicion y tamaño de la ventana.
        self.line_edit = QLineEdit(self) # Se creo un objeto/widget de una linea de edicion y como parametro se paso a la ventana (self)
        self.push_button = QPushButton("Submit",self) # Se creo como objeto un boton 
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10, 10, 200, 40)# Se edito la linea de edicion
        self.line_edit.setStyleSheet("Font-size: 20px;"
                                     "Font-family: Arial;")
        self.push_button.setGeometry(210,10,100,40) # Se edito el boton.
        self.push_button.setStyleSheet("Font-size: 20px;"
                                       "Font-family: Arial;")
        
        self.line_edit.setPlaceholderText("Enter your name") # El metodo setPlaceholderText sirve para poner un texto en el fondo de la linea.
        
        self.push_button.clicked.connect(self.submit) # Se creo un evento para cuando se presione el boton.
        
    def submit(self):
        text = self.line_edit.text() # Con esto se obtiene el texto que se introduce a la linea de edicion.
        print(f"Hello {text}")   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())