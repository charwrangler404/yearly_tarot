import sys
import random
from lib import func
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.cards = {0:"The Fool", 1:"The Magicican", 2:"The High Priestess", 3:"The Empress", 4:"The Emperor",
         5:"The Hirophant", 6:"The Lovers", 7:"The Chariot", 8:"Strength", 9:"The Hermit",
         10:"Wheel of Fortune", 11:"Justice", 12:"The Hanged Man", 13:"Death", 14:"Temperance",
         15:"The Devil", 16:"The Tower", 17:"The Star", 18:"The Moon", 19:"The Sun", 
         20:"Judgement", 21:"The World"}
        
        self.button = QtWidgets.QPushButton("Calculate")
        self.text = QtWidgets.QLabel("Enter your birth month and day, and the year you wish to ask about",
                                     alignment=QtCore.Qt.AlignCenter)
        
        self.cal = QtWidgets.QCalendarWidget()
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.cal)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        date = self.cal.selectedDate()
        card = self.cards[func.iterate(date.day() + date.month() + date.year())]
        self.text.setText(card)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.setWindowTitle("Yearly Card")
    widget.resize(400, 400)
    widget.show()

    sys.exit(app.exec())