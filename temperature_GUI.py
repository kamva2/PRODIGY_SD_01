# Kamva Poswa
# 18 June 2024

import sys
from PyQt5.QtWidgets import *

class TemperatureConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.init_GUI()

    def init_GUI(self):
        self.setWindowTitle('Temperature Converter')
        self.setGeometry(250, 250, 400, 200)

        self.label = QLabel('Enter temperature:')
        self.text = QLineEdit()
        self.result = QLabel('Results here.')

        self.convert_button = QPushButton('Convert')
        self.close_button = QPushButton('Close')
        self.convert_button.clicked.connect(self.convert_temperature)
        self.close_button.clicked.connect(self.close)        

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.text)
        vbox.addWidget(self.result)
        vbox.addWidget(self.convert_button)
        vbox.addWidget(self.close_button)

        self.setLayout(vbox)

    def convert_temperature(self):
        x = self.text.text()
        temp = spliting(x)
        float_temp = float(temp[0])
        str_temp = str(' '.join(temp[1:]).lower())

        if str_temp == "degree celsius":
            kelvin = float_temp + 273.15
            fahrenheit = (float_temp * 9/5) + 32
            result = f"The temperature is {round(kelvin, 2)}K in Kelvin.\n"
            result += f"The temperature is {round(fahrenheit, 2)}F in Fahrenheit."

        elif str_temp == "kelvin":
            degree_c = float_temp - 273.15
            fahrenheit = (float_temp - 273.15) * 5/9 + 32
            result = f"The temperature is {round(degree_c, 2)}C in Celsius.\n"
            result += f"The temperature is {round(fahrenheit, 2)}F in Fahrenheit."

        elif str_temp == "fahrenheit":
            degree_c = (float_temp - 32) * 5/9
            kelvin = (float_temp - 32) * 5/9 + 273.15
            result = f"The temperature is {round(degree_c, 2)}C in Celsius.\n"
            result += f"The temperature is {round(kelvin, 2)}K in Kelvin."

        else:
            result = "Please enter (kelvin, fahrenheit, degree celsius) temperature!!!"

        self.result.setText(result)
        self.text.clear()
    def close(self):
        self.close()

def spliting(x):
    return x.split()

def main():
    app = QApplication(sys.argv)
    convert = TemperatureConverter()
    convert.show()
    sys.exit(app.exec_())
main()