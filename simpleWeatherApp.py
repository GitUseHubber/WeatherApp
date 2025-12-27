import requests
import sys
import pygame
from PyQt6.QtWidgets import (QApplication,QWidget,QLabel,QPushButton,
                                QLineEdit,QBoxLayout,QGridLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon,QPixmap,QFont



api_key = "your_api_key"
class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather APP") #Name of the window
        icon = QIcon("iconImage.png") #Making the icon
        self.setWindowIcon(icon) #Setting the icon to the app
        self.setFixedSize(300,300)

        #! Setting Layout
        global layout
        layout = QGridLayout()
        self.setLayout(layout)
        
        #Title of the APP
        self.label1 = QLabel("Weather APP")
        self.label1.setFont(QFont("Arel",20,QFont.Weight.Bold))
        self.label1.setStyleSheet("color: white;")
        layout.addWidget(self.label1,0,0,Qt.AlignmentFlag.AlignHCenter)

        #Bold Lines for aesthetic purpose
        self.line = QLabel("-------------------------------------")
        self.line.setFont(QFont("Arel",12,weight=QFont.Weight.Bold))
        layout.addWidget(self.line,1,0,Qt.AlignmentFlag.AlignCenter)

        #Enter city name
        self.label2 = QLabel("Enter a city name")
        self.label2.setFont(QFont("Arel",15,QFont.Weight.ExtraBold))
        self.label2.setStyleSheet("color: orange;")
        layout.addWidget(self.label2,2,0,Qt.AlignmentFlag.AlignCenter)

        #Bold Lines for aesthetic purpose
        self.line1 = QLabel("-------------------------------------")
        self.line1.setFont(QFont("Ariel",12,weight=QFont.Weight.Bold))
        layout.addWidget(self.line1,3,0,Qt.AlignmentFlag.AlignCenter)

        
        #Text Editor
        self.input1 = QLineEdit()
        self.input1.setFont(QFont("Comic Sans",12,QFont.Weight.Bold))
        self.input1.setFixedSize(130,30)
        layout.addWidget(self.input1,4,0,Qt.AlignmentFlag.AlignHCenter)
        

        #The button
        self.button = QPushButton("Enter")
        self.button.setFont(QFont("Ariel",10,QFont.Weight.Bold))
        self.button.setStyleSheet("background-color: orange; color: white;")
        self.button.clicked.connect(self.get_display_data) #Linking the button to the get_display_data method.
        self.button.setFixedSize(100,20)
        layout.addWidget(self.button,6,0,Qt.AlignmentFlag.AlignCenter)

        #Initializing an empty label to change it later
        self.labeln = QLabel("")
        layout.addWidget(self.labeln)

        #Emoji
        self.emoji = QLabel("")
        layout.addWidget(self.emoji)
        #Description
        self.description = QLabel("")
        layout.addWidget(self.description)
        

    #How the button functions 
    def get_display_data(self):
        city_name = self.input1.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
        response = requests.get(url)
        code = response.status_code
        global data
        data = response.json()
        if code == 200:
            temp_in_celsius = round(float(data["main"]["temp"])-273.15)
            self.labeln.clear()
            self.labeln = QLabel(str(temp_in_celsius)+"°C")
            self.labeln.setFont(QFont("Ariel",15,QFont.Weight.DemiBold))
            layout.addWidget(self.labeln,7,0,Qt.AlignmentFlag.AlignCenter)
            if  200 <= data["weather"][0]["id"] <= 232:
                self.emojiUpdate("🌩️")
                self.descriptionUpdate()
            elif  300 <= data["weather"][0]["id"] <= 321:
                self.emojiUpdate("🌦️")
                self.descriptionUpdate()
            elif  500 <= data["weather"][0]["id"] <= 531:
                self.emojiUpdate("🌧️")
                self.descriptionUpdate()
            elif  600 <= data["weather"][0]["id"] <= 622:
                self.emojiUpdate("❄️")
                self.descriptionUpdate()
            elif  701 <= data["weather"][0]["id"] <= 781:
                self.emojiUpdate("🌫️")
                self.descriptionUpdate()
            elif  801 <= data["weather"][0]["id"] <= 804:
                self.emojiUpdate("☁️")
                self.descriptionUpdate()
            elif data["weather"][0]["id"] == 800:
                self.emojiUpdate("☀️")
                self.descriptionUpdate()
        else:
            self.labeln.clear()
            self.emoji.clear()
            self.description.clear()
            self.labeln = QLabel("City not found!")
            self.labeln.setFont(QFont("Ariel",15,QFont.Weight.DemiBold))
            layout.addWidget(self.labeln,7,0,Qt.AlignmentFlag.AlignCenter)

    def emojiUpdate(self,emoji):
        self.emoji.clear()
        self.emoji = QLabel(emoji)
        self.emoji.setFont(QFont("Ariel",30))
        layout.addWidget(self.emoji,9,0,Qt.AlignmentFlag.AlignCenter)
    def descriptionUpdate(self):
        self.description.clear()
        self.description = QLabel(data["weather"][0]["description"])
        self.description.setFont(QFont("Ariel",15,QFont.Weight.DemiBold))
        layout.addWidget(self.description,8,0,Qt.AlignmentFlag.AlignCenter)
    

#Executing here
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    window.setStyleSheet("background-color: #ADD8E6;")
    window.show()
    sys.exit(app.exec())



