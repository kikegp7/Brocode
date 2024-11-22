# Python stopwatch program

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QTime, QTimer

class Stopwatch(QWidget):

    def __init__(self):
        super().__init__()
        self.time_label = QLabel("00:00:00:00", self) # Se crean los siguientes elementos que usare en mi widget el cual son
        self.start_button = QPushButton("Start", self) # Un label, 3 botones, un tiempo y un temporizador.
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.time = QTime(0,0,0,0)
        self.timer = QTimer(self)
        self.initUI() # Se inicializa el metodo initUI
    

    def initUI(self):
        self.setWindowTitle("Stopwatch") # Establecemos el titulo de la ventana 
        #self.setGeometry(800, 400, 600, 250)

        vbox = QVBoxLayout() # Creamos un layout vertical y le añadimos el label. 
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)    
        self.time_label.setAlignment(Qt.AlignCenter) #Alineamos el label al centro del widget

        
        hbox = QHBoxLayout() # Creamos un layout horizontal y le añadimos los 3 botones 
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox) #Añadimos estos layout horizontales al layout vertical previamente establecido.

        self.setStyleSheet("""
                        QPushButton{
                            font-size: 60px;
                        }
                        QLabel{
                            font-size: 120px;
                            background: #96efff;
                        }
                        """)
        
        # Le damos formato y cambios a los botones y al label.

        self.start_button.clicked.connect(self.start)   # Creamos un evento para cuando se presione el boton start. 
        self.stop_button.clicked.connect(self.stop)     # Creamos un evento para cuando se presione el boton stop. 
        self.reset_button.clicked.connect(self.reset)   # Creamos un evento para cuando se presione el boton reset. 
        self.timer.timeout.connect(self.update_display) # Creamos un evento para cuando se ejecute un timeout. 


        
    def start(self):
        self.timer.start(10) #Hacemos que el temporizador empiece en intervalos de 10 ms.

    def stop(self):
        self.timer.stop() # Detenemos el temporizador.

    def reset(self):
        self.timer.stop()                                       #Detenemos el temporizador
        self.time = QTime(0,0,0,0)                              #Generamos un nuevo objeto time con los valores 0,0,0,0 (h,m,s,ms).
        #self.time_label.setText("00:00:00:00")
        self.time_label.setText(self.format_time(self.time))    #Le pasamos este nuevo valor al label para que lo muestre.

    def format_time(self, time):    #Aqui le damos formato al tiempo para poder regresar un str y añadirlo al metodo setText del label.
        hours = time.hour()         #Obtenemos la hora.
        minutes = time.minute()     #Obtenemos los minutos.
        seconds = time.second()     #Obtenemos los segundos.
        miliseconds = time.msec() // 10     #Obtenemos los milisegundos y se divide entre 10 para quitar los 3 digitos.
        return f"{hours:02}:{minutes:02}:{seconds:02}.{miliseconds:02}" #Aqui se regresa en formato str los valores con solo 2 digitos.

    def update_display(self):
        self.time = self.time.addMSecs(10) # Se le añade al tiempo 10 ms
        self.time_label.setText(self.format_time(self.time))    # Se muestra la informacion.


if __name__ == "__main__":
    app = QApplication(sys.argv)
    watch = Stopwatch()
    watch.show()
    sys.exit(app.exec_())