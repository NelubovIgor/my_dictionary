import csv
import sys
import random
from PySide6 import QtCore, QtWidgets


def load_file(name_file):
    with open(name_file, 'r', encoding='utf-8') as text:
        line = text.readline()

        list_words = []

        while line != '':
            list_words.append(line.strip())
            line = text.readline() 

        sorted_dictionary = sorted(list_words)
    return sorted_dictionary


def save_file(sorted_dictionary):
    with open('english_dictionary.csv', 'w', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",")
        for w in sorted_dictionary:
            eng, rus = w.split(' - ')
            file_writer.writerow([eng, rus])
        print('готово')


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
