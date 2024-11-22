# Digital clock with Python

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):

    def __init__(self):
        super().__init__()              # Se usa super() para poder acceder al constructor de la clase padre y a sus atributos y metodos.
        self.time_label = QLabel(self)  # Se crea un atributo de la clase Qlabel que es donde mostraremos los datos
        self.timer = QTimer(self)       # Se crea un atributo de la clase QTimer para poder obtener el tiempo actual.
        self.initUI()

    
    def initUI(self):
        self.setWindowTitle("Digital Clock")    # Se establece el titulo de la ventana (widget)
        self.setGeometry(800, 400, 300, 100)    # Se establece la posicion y el tamaño del widget

        vbox = QVBoxLayout()                    # Se genera un layout vertical para poner los elementos que sera solo un label.
        vbox.addWidget(self.time_label)         # Añadimos el elemento (label) al layout vertical con el metodo addWidget
        self.setLayout(vbox)                    # Establecemos en el widget (ventana) el layout vertical para poder visualizarlo

        self.time_label.setAlignment(Qt.AlignCenter)                # El elemento (label) alineamos de manera central al widget
        self.time_label.setStyleSheet("font-size: 150px;"           # El elemento (label) le modificamos su tamaño y color.
                                      "color: hsl(136, 96%, 49%);")
        self.setStyleSheet("background: black;")                    # Modificamos el color de fondo del widget. 

        font_id = QFontDatabase.addApplicationFont("Brocode/DS-DIGIT.TTF")  # Creamos un font_id del font nuevo que queremos importar y usar.
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]     # Creamos un font_family y le paso de parametros el font_id[0] posicion 0.
        my_font = QFont(font_family, 150)                                   # Creamos un objeto de la clase QFont y de parametro le ingresamos el font_family y el tamaño del punto
        self.time_label.setFont(my_font)                                    # Por ultimo al elemento (label) le establecemos el nuevo Font_Family (estilo de letra).

        self.timer.timeout.connect(self.update_time)    # Se crea un evento para que cuando pase ejecute el metodo update_time()
        self.timer.start(1000)                          # Se pone una pausa de 1 segundo para despues volver a ejecutar el evento

        self.update_time()                              

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")    # Se obtiene el tiempo actual en formato Hora:minutos:segundo AM/PM
        self.time_label.setText(current_time)                         # Se visualiza esta informacion en el label.


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())