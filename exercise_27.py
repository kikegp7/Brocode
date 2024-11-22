# PyQt5 Checkboxes

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow): #Se crea una clase hijo que va a heredear todos los atributos y metodos de la Clase padre que en este caso es QMainWindow

    def __init__(self):     # Se crea un constructor para la clase hijo
        super().__init__()      #Se usa super() para poder acceder al constructor de la clase padre y a sus atributos y metodos.
        self.setGeometry(700, 300, 500, 500)  #El metodo setGeometry(x,y,width,height) nos permite modificar la posicion y tamaño de la ventana.
        self.checkbox = QCheckBox("Do you like food?", self) # Se crea un atributo de la clase QCheckBox("Mensaje str", self)
        self.initUI()   # Se llama al metodo initUI para que cuandos e construya un objeto de la clase MainWindow se llame de manera automatica.

    def initUI(self): # Se define un metodo de initUI para tener un mejor orden y recibe como parametro la ventana misma osea self
        self.checkbox.setGeometry(10, 0, 500, 100) # Se modifica el tamaño y posicion del checkbox
        self.checkbox.setChecked(False) # El metodo setChecked sirve para establercer que la caja este sin checar o checada
        self.checkbox.stateChanged.connect(self.checkbox_changed) # Se crea un evento con stateChanged lo cual nos dira que si se chequea el cuadro sucedera un evento que sera una funcion.
    
    def checkbox_changed(self, state): # Se crea una funcion que hara cuando se active el evento de checar o unchecar.
        if state == Qt.Checked: # cuando el estado esta en 2 es porque se checo y 0 cuando se uncheco pero para hacerlo mas leible se usa
            print("You like food!") #Qt.Checked que es lo mismo que 2.
        else:
            print("You don't like food!")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())