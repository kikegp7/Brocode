# PyQt5 layouts

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout

class MainWindow(QMainWindow): #Se crea una clase hijo que va a heredear todos los atributos y metodos de la Clase padre que en este caso es QMainWindow

    def __init__(self):     # Se crea un constructor para la clase hijo
        super().__init__()      #Se usa super() para poder acceder al constructor de la clase padre y a sus atributos y metodos.
        self.setGeometry(700, 300, 500, 500)  #El metodo setGeometry(x,y,width,height) nos permite modificar la posicion y tamaño de la ventana.
        self.initUI()   # Se llama al metodo initUI para que cuandos e construya un objeto de la clase MainWindow se llame de manera automatica.

    def initUI(self): # Se define un metodo de initUI para tener un mejor orden y recibe como parametro la ventana misma osea self
        central_widget = QWidget() # Se crea un objeto de la clase QWidget() 
        self.setCentralWidget(central_widget) # Se llama a la ventana misma con el self y se usa el metodo setCentralWidget y se pasa de parametro un objeto de la clase Qwidget

        label1 = QLabel("#1",self)  # Se crean 5 objetos o labels
        label2 = QLabel("#2",self)
        label3 = QLabel("#3",self)
        label4 = QLabel("#4",self)
        label5 = QLabel("#5",self)

        label1.setStyleSheet("background-color: red;") # Se modifica el color del fondo de estos 5 objetos o labels
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: blue;")
        label5.setStyleSheet("background-color: purple;")

        vbox = QVBoxLayout() 
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)
        """
        grid = QGridLayout()    # Se crea un objeto de la clase QGridLayout para poder acomodar los objetos en la ventana y visualizarlos.
        grid.addWidget(label1, 0, 0)  # Se usa el metodo addWidget(label, row, column) para poder pasarle el label al widget y su posicion
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)
        grid.addWidget(label5, 2, 0)
        """
        central_widget.setLayout(vbox) # Por ultimo para visualizar los widgets en la ventana se usa el metodo setLayout() y se le pasa
                                       # el objeto de la clase grid o vbox o hbox 
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()