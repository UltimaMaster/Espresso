import sqlite3
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem


class MainWindowCoffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.select_data)

    def select_data(self):
        # Подключаемся к базе
        connection = sqlite3.connect("coffee.sqlite")
        # Делаем запрос и получаем данные
        query = "SELECT * FROM coffee"
        res = connection.cursor().execute(query).fetchall()
        # Заполним размеры таблицы
        self.tableWidget.setColumnCount(len(res[0]) - 1)
        self.tableWidget.setRowCount(len(res))
        self.tableWidget.setHorizontalHeaderLabels(["Название", "Обжарка", "Тип", "Вкус", "Цена", "Объем"])
        # Заполняем таблицу элементами
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            # Игнорируем данные id
            for j, elem in enumerate(row[1:]):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindowCoffee()
    ex.show()
    sys.exit(app.exec())
