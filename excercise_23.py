#PyQt5 introduction windows, labels

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow): #Se crea una clase hijo que va a heredear todos los atributos y metodos de la Clase padre que en este caso es QMainWindow

    def __init__(self):     # Se crea un constructor para la clase hijo
        super().__init__()      #Se usa super() para poder acceder al constructor de la clase padre y a sus atributos y metodos.
        self.setWindowTitle("My first GUI.")  #El metodo setWindowTitle(str) nos permite cambiar el titulo de la ventana.
        self.setGeometry(700, 300, 500, 500)  #El metodo setGeometry(x,y,width,height) nos permite modificar la posicion y tamaño de la ventana.
        self.setWindowIcon(QIcon("Brocode\Aeriak-logotipo_RBG-01.jpg")) #El metodo setWindowIcon(QIcon(str de la direccion de la imagen)) permite añadir una imagen como icono de la ventana
        
        label = QLabel("Hello", self)  # Creamos un objeto de la clase Qlabel(mensaje, self)
        label.setFont(QFont("Arial", 40)) # Modificamos con el metodo setFont(QFont(estilo de letra, tamaño)) el contenido.
        label.setGeometry(0,0,500,100)  # Con este metodo setGeometry(x,y, width, height) modificamos la posicion y tamaño del contenido.
        label.setStyleSheet("color:#28521a;"                # Con el metodo setStyleSheet(color background-color font-weight font-style text-decoration) 
                            "background-color: #9de3fa;"    # Podemos modiciar desde el color del contenito, el fondo, el estilio, si es negrita o no, etc.
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        #label.setAlignment(Qt.AlignTop)    # Vertical Top
        #label.setAlignment(Qt.AlignBottom)    # Vertical Bottom
        #label.setAlignment(Qt.AlignVCenter)    # Vertical Center

        #label.setAlignment(Qt.AlignRight)    # Horizontally Right
        #label.setAlignment(Qt.AlignHCenter)    # Horizontally Center
        #label.setAlignment(Qt.AlignLeft)    # Horizontally Left

        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # Alinear de manera central y arriba

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()