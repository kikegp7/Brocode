# PyQt5 Push buttons


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class MainWindow(QMainWindow): #Se crea una clase hijo que va a heredear todos los atributos y metodos de la Clase padre que en este caso es QMainWindow

    def __init__(self):     # Se crea un constructor para la clase hijo
        super().__init__()      #Se usa super() para poder acceder al constructor de la clase padre y a sus atributos y metodos.
        self.setGeometry(700, 300, 500, 500)  #El metodo setGeometry(x,y,width,height) nos permite modificar la posicion y tamaño de la ventana.
        self.button = QPushButton("Click Me!", self) #Se inicializa en el constructor el atributo button
        self.label = QLabel("Hello", self) #Se inicializa en el constructor el atributo label
        self.initUI()   # Se llama al metodo initUI para que cuandos e construya un objeto de la clase MainWindow se llame de manera automatica.

    def initUI(self): # Se define un metodo de initUI para tener un mejor orden y recibe como parametro la ventana misma osea self
        self.button.setGeometry(150, 200, 200, 100) # Se modifica la geometria (tamaño y posicion) del boton
        self.button.setStyleSheet("font-size: 30px;") # Se cambia el tamaño del mensaje interior del boton. 
        self.button.clicked.connect(self.on_click) # Se genera un evento. el clicked es un evento y el connect(funcion) es una accion que pasara si ocurre ese evento.

        self.label.setGeometry(150, 300, 200, 100) # Se modifica la geometria (tamaño y posicion) del label.
        self.label.setStyleSheet("font-size: 50px") # Se cambia el tamaño del mensaje interior del label. 

    def on_click(self): # Se genera una función que va hacer una accion cuando se ejecute el boton. 
        self.label.setText("Goodbye!") #Establecemos que el label que al inicio es Hello cambiara a Goodbye cuando se ejecute el boton.
        self.button.setDisabled(True) # El metodo setDisabled(boolean) nos permite establecer que solo se presione el boton 1 vez.
        
        


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()