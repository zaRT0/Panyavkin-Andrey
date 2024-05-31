import sys
import logging

from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QPushButton,
    QLabel,
    QLineEdit
)
from PyQt5.QtGui import QPixmap

from cash import Hash
from reading_and_writing_data import Functions
from constants import PATH, DATA


logging.basicConfig(level=logging.INFO)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Card number programm")

        self.background_style = f"background-color: white;"
        self.button_style = f"background-color: gray; border: 5px solid #585A56; border-radius:10px"
        self.label_style = f"font-size: 16px; border-radius: 10px 10px; background-color: #C2D3DA; padding: 10px;"
        self.line_style = f"{self.label_style} color: hsla(0, 0%, 0%, 0.5);"
        self.border_style = f"background-color: white; border: 5px solid #585A56; border-radius:20px"

        self.setFixedSize(950, 750)
        self.setStyleSheet(self.background_style)

        self.border1 = QLabel(self)
        self.border1.setGeometry(70, 10, 810, 70)
        self.border1.setStyleSheet(self.border_style)

        self.hash = QLineEdit("ХЭШ", self)
        self.hash.setGeometry(80, 20, 120, 50)
        self.hash.setStyleSheet(self.line_style)

        self.bin = QLineEdit("БИН", self)
        self.bin.setGeometry(210, 20, 120, 50)
        self.bin.setStyleSheet(self.line_style)

        self.last_numbers = QLineEdit("4 цифры", self)
        self.last_numbers.setGeometry(340, 20, 120, 50)
        self.last_numbers.setStyleSheet(self.line_style)

        self.number_button = QPushButton("УЗНАТЬ", self)
        self.number_button.setGeometry(470, 20, 80, 50)
        self.number_button.setStyleSheet(self.button_style)

        self.card_number_line = QLabel("Номер карты", self)
        self.card_number_line.setGeometry(560, 20, 310, 50)
        self.card_number_line.setStyleSheet(self.label_style)

        self.border2 = QLabel(self)
        self.border2.setGeometry(70, 90, 810, 70)
        self.border2.setStyleSheet(self.border_style)

        self.luhn_card = QLineEdit("Номер карты", self)
        self.luhn_card.setGeometry(80, 100, 270, 50)
        self.luhn_card.setStyleSheet(self.line_style)

        self.luhn_button = QPushButton("ПРОВЕРИТЬ ПО АЛГОРИТМУ ЛУНА", self)
        self.luhn_button.setGeometry(360, 100, 250, 50)
        self.luhn_button.setStyleSheet(self.button_style)

        self.card_validity = QLabel("Действительность карты", self)
        self.card_validity.setGeometry(620, 100, 250, 50)
        self.card_validity.setStyleSheet(self.label_style)

        self.border3 = QLabel(self)
        self.border3.setGeometry(70, 170, 810, 560)
        self.border3.setStyleSheet(self.border_style)

        self.graphic_button = QPushButton("ПОСТРОИТЬ ГРАФИК", self)
        self.graphic_button.setGeometry(390, 180, 200, 50)
        self.graphic_button.setStyleSheet(self.button_style)

        self.graphic = QLabel(self)
        self.graphic.setGeometry(500, 500, 1, 1)

        self.number_button.clicked.connect(self.create_card_number)
        self.luhn_button.clicked.connect(self.luhns_algorithm)
        self.graphic_button.clicked.connect(self.create_graphic)

    def create_card_number(self):
        hash_value = self.hash.text()
        last_numbers_value = self.last_numbers.text()
        bin_value = self.bin.text().split(", ")
        card_number = Hash.create_card_number(hash_value, bin_value, last_numbers_value)
        if card_number:
            self.card_number_line.setText(card_number)
        else:
            self.card_number_line.setText("Не удалось найти номер карты")

    def luhns_algorithm(self):
        card_number_value = self.luhn_card.text()
        validity = Hash.luhns_algorithm(card_number_value)
        if validity:
            self.card_validity.setText("Карта действительна")
        else:
            self.card_validity.setText("Карта недействительна")

    def create_graphic(self):
        paths = Functions.read_json_file(PATH)
        data = Functions.read_json_file(DATA)
        Hash.time_for_find_collisions(data["hash"], data["last_four_numbers"], data["bin"], paths["graphic_path"])
        pixmap = QPixmap(paths["graphic_path"])
        self.graphic.setGeometry(80, 230, 790, 474)
        pixmap = pixmap.scaled(790, 474)
        self.graphic.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    application = MainWindow()
    application.show()
    sys.exit(app.exec_())