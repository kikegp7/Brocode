# Weather app using Python

import sys
import requests
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt
from weather_key import key


class WeatherApp(QWidget):

    def __init__(self):
        super().__init__()
        self.label_city = QLabel("Enter city name:", self)
        self.label_degrees = QLabel(self)
        self.label_clouds = QLabel(self)
        self.sumbit_button = QPushButton("Get Weather",self)
        self.emoji_label = QLabel(self)
        self.line_edit = QLineEdit(self)
        self.initUI()
    
    
    def initUI(self):

        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addWidget(self.label_city)
        vbox.addWidget(self.line_edit)
        vbox.addWidget(self.sumbit_button)
        vbox.addWidget(self.label_degrees)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.label_clouds)
        
        self.label_city.setAlignment(Qt.AlignCenter)
        self.line_edit.setAlignment(Qt.AlignCenter)
        self.label_degrees.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.label_clouds.setAlignment(Qt.AlignCenter)
        self.setLayout(vbox)

        self.line_edit.setPlaceholderText("City name")

        self.label_city.setObjectName("label_city")
        self.line_edit.setObjectName("line_edit")
        self.sumbit_button.setObjectName("push_button")
        self.label_degrees.setObjectName("label_degrees")
        self.emoji_label.setObjectName("emoji_label")
        self.label_clouds.setObjectName("label_clouds")

        self.setStyleSheet("""
                        QLabel, QPushButton{
                            font-family: Calibri;
                        }
                        QLabel#label_city{
                            font-size: 40px;
                            font-style: italic;
                            margin-bottom: 5px;
                        }   
                        QLineEdit{
                            font-size: 40px;
                            border: 1px solid;
                           }
                        QPushButton{
                            font-size: 30px;
                            font-weight: bold;
                           }   
                        QLabel#label_degrees{
                            font-size: 75px;
                            font-weight: 500;
                           }
                        QLabel#emoji_label{
                            font-size: 100px;
                            font-family: Segoe UI emoji;                       
                           }   
                        QLabel#label_clouds{
                            font-size: 50px;
                           }
                        """)
        
        self.sumbit_button.clicked.connect(self.get_weather)


    def get_weather(self):
        city_name = self.line_edit.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&lang=es&appid={key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            if response.status_code == 200:
                weather_data = response.json()
                self.display_weather(weather_data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request:\nPlease check your input.")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API key.")
                case 403:
                    self.display_error("Forbidden:\nAcces is denied.")
                case 404:
                    self.display_error("Not Found:\nCity not found.")
                case 500:
                    self.display_error("Internal Server Error:\nPlease try again later.")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from the server.") 
                case 503:
                    self.display_error("Service Unavailable:\nServer is down.")
                case 504:
                    self.display_error("Gateway Timeout:\nNo response from the server.")
                case _:
                    self.display_error(f"HTTP Error Ocurred:\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\n Check your internet connection.")

        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out.")

        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many TooManyRedirects:\nCheck your url.")

        except requests.exceptions.RequestException as req_error: #URL Invalido o problemas de red.
            self.display_error(f"Request error\n{req_error}")


    def display_error(self, message):
        self.label_degrees.setStyleSheet("font-size: 30px;")
        self.label_degrees.setText(message)
        self.emoji_label.clear()
        self.label_clouds.clear()

    def display_weather(self, data):
        self.label_degrees.setStyleSheet("font-size: 75px;")
        temperature_k = data["main"].get("temp")
        temperature_c= float(temperature_k) - 273.15
        weather_description = data["weather"][0].get("description")
        weather_id = data["weather"][0].get("id")
        weather_emoji = self.get_weather_emoji(weather_id)
        
        self.label_degrees.setText(f"{temperature_c:.0f}°C")
        self.emoji_label.setText(weather_emoji)
        self.label_clouds.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):
        if weather_id >= 200 and weather_id <=232:
            return "🌩️"
        elif weather_id >=300 and weather_id <=321:
            return ".🌦️"
        elif weather_id >=500 and weather_id <=531:
            return "🌧️"
        elif weather_id >=600 and weather_id <=622:
            return "🌨️"
        elif weather_id >=700 and weather_id <=741:
            return "🌫️"
        elif weather_id == 781:
            return "-🌪️"
        elif weather_id == 800:
            return "☀️"
        elif weather_id > 800 and weather_id <= 804:
            return "☁️"
        else:
            return ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())    
