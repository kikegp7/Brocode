# PyQt5 Radio Buttons

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

class MainWindow(QMainWindow): #Se crea una clase hijo que va a heredear todos los atributos y metodos de la Clase padre que en este caso es QMainWindow

    def __init__(self):     # Se crea un constructor para la clase hijo
        super().__init__()      #Se usa super() para poder acceder al constructor de la clase padre y a sus atributos y metodos.
        self.setGeometry(700, 300, 500, 500)  #El metodo setGeometry(x,y,width,height) nos permite modificar la posicion y tamaño de la ventana.
        self.radio1 = QRadioButton("Visa", self) # Se definen 5 widgets (objetos) de botones de radio.
        self.radio2 = QRadioButton("Mastercard", self)
        self.radio3 = QRadioButton("Gift Card", self)
        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("Online", self)
        self.button_group1 = QButtonGroup(self) # Se define 2 grupos de botones 
        self.button_group2 = QButtonGroup(self)
        self.initUI()   # Se llama al metodo initUI para que cuandos e construya un objeto de la clase MainWindow se llame de manera automatica.

    def initUI(self): # Se define un metodo de initUI para tener un mejor orden y recibe como parametro la ventana misma osea self
        self.radio1.setGeometry(0, 0, 300, 50) # Se modifica la posición ,ancho y altura de los widgets.
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)
        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)

        self.setStyleSheet("QRadioButton{"      # Se modifica el estilo de los 5 objetos de radios o widgets
                           "font-size: 40px;"
                           "font-family: Arial;"
                           "padding: 10px;"
                           "}")
        
        self.button_group1.addButton(self.radio1) # Se añaden los 3 primeros widgets a un grupo de botones esto para que solo se puedan elegir una opcion entre esos tres.
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)

        self.button_group2.addButton(self.radio4) # Se añaden los 2 ultimos widgets a un grupo de botones esto para que solo se puedan elegir una opcion entre esos dos.
        self.button_group2.addButton(self.radio5)
        
        self.radio1.toggled.connect(self.radio_button_changed) # Se ejecuta un evento, cuando se selecciona a uno de estos botones hara una funcion.
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)


    def radio_button_changed(self):    # Se define una funcion que se activara cuando se presione el check de uno de estos botones de radio.
        radio_button = self.sender()    # El metodo sender() nos indica que widget en la memoria fue el que se activo.
        if radio_button.isChecked():    # El metodo isChecked() nos regresa un booleano True si se presiono un evento.
            print(f"{radio_button.text()} is selected.") #se usa el metodo text() para que nos indique el texto o informacion del evento que se activo.


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())