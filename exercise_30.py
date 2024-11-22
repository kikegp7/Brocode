import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()      #Se usa super() para poder acceder al constructor de la clase padre y a sus atributos y metodos.
        self.button1 = QPushButton("#1") # Se crearon 3 objetos de la clase de botones. Esta vez no se inicializaron a la ventana porque
        self.button2 = QPushButton("#2") # se van a inicializar hacia un center manangemet 
        self.button3 = QPushButton("#3")
        self.initUI()

    def initUI(self):
        central_widget = QWidget(self) # Primero se crea un objeto de la clase Qwidget por lo que creamos un widget primero
        self.setCentralWidget(central_widget) # Establecemos el central wigdet a la pantalla de parametro le paso un objeto Qwidget

        hbox = QHBoxLayout() # Creamos un objeto de la clase QHBoxLayout para poder añadir los botones al widget.

        hbox.addWidget(self.button1) # Agregamos cada boton al widget.
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        central_widget.setLayout(hbox) # Establecemos los botones para que se puedan ver.

        self.button1.setObjectName("button1") #Le ponemos un nombre a cada objeto del boton para despues poder usarlos en su estilo
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
            QPushButton{
                font-size: 40px;
                font-family: Arial;
                padding: 15px 75px;  
                margin: 25px;
                border: 3px solid;  
                border-radius: 15px;       
            }
            QPushButton#button1{
                background: #fa5c5f;       
            }
            QPushButton#button2{
                background: #5cfa99;       
            }
            QPushButton#button3{
                background: #2e3cff;       
            }
        """)
                            # Establecemos con self.setStyleSheet el cambio para todos los elementos del widget
                            # QPushButton se menciona al nombre para abarcar a todo el grupo
                            # Despues individualmente con QPushButton#nombredelobjeto es para editar de manera individual
                            # Margin es el espacio entre los widgets
                            # border es para los bordes de los botones
                            # border radius sirve para redondear las esquinas

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())