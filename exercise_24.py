# PyQt5 Images

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow): #Se crea una clase hijo que va a heredear todos los atributos y metodos de la Clase padre que en este caso es QMainWindow

    def __init__(self):     # Se crea un constructor para la clase hijo
        super().__init__()      #Se usa super() para poder acceder al constructor de la clase padre y a sus atributos y metodos.
        self.setGeometry(700, 300, 500, 500)  #El metodo setGeometry(x,y,width,height) nos permite modificar la posicion y tamaño de la ventana.

        label = QLabel(self) # Se crea un label para poder manipular la imagen, se usa el self porque esta llamando a si mismo a la ventana.
        label.setGeometry(0, 0, 250, 250) # Se establece el tamaño de la imagen.

        pixmap = QPixmap("Brocode\Aeriak-logotipo_RBG-01.jpg") # Se crea la imagen mediante un objeto pixmap = QPixmap(str de la direccion de la imagen)
        label.setPixmap(pixmap) # Se llama a la imagen mediante setPixmap(un objeto pixmap)
        label.setScaledContents(True) # Se escala el contenido de acuerdo al tamaño establecido anteriormente en label.setGeometry

        label.setGeometry((self.width()- label.width())//2 , (self.height()- label.height()) // 2, label.width(), label.height()) 
        # Se le da nuevos de posicion a la imagen.

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()