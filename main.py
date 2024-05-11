import sys
import csv
from PySide6.QtWidgets import (QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget,
                               QPushButton, QLineEdit, QLabel, QHBoxLayout, QFileDialog, QInputDialog)


class DictionaryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Словарь")
        self.setGeometry(100, 100, 800, 600)

        # Создаем таблицу для отображения словаря
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Английское слово", "Перевод"])
        self.table.setSortingEnabled(True)

        # Создаем поле для поиска слова
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Поиск слова...")

        # Создаем кнопку для добавления нового слова
        self.add_button = QPushButton("Добавить слово")
        self.add_button.clicked.connect(self.add_word)

        # Создаем вертикальный контейнер для элементов интерфейса
        layout = QVBoxLayout()
        layout.addWidget(self.search_input)
        layout.addWidget(self.table)
        layout.addWidget(self.add_button)

        # Создаем главный виджет и устанавливаем в него вертикальный контейнер
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Загружаем словарь из CSV-файла (замените путь к файлу на свой)
        self.load_dictionary("english_dictionary.csv")

    def load_dictionary(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                reader = csv.reader(file)

                for row in reader:
                    if row:
                        # print(row)
                        english_word, translation = row
                        self.add_word_to_table(english_word, translation)
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")

    def add_word_to_table(self, english_word, translation):
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(english_word))
        self.table.setItem(row_position, 1, QTableWidgetItem(translation))

    def add_word(self):
        english_word = self.search_input.text()
        translation, ok = QInputDialog.getText(self, "Добавить слово", f"Введите перевод для слова '{english_word}':")
        if ok and translation:
            self.add_word_to_table(english_word, translation)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DictionaryApp()
    window.show()
    sys.exit(app.exec_())
