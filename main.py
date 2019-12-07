import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QMainWindow


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect("coffee.db")
        cur = self.con.cursor()
        result = list(cur.execute("Select * from Coffee").fetchall())
        for i in range(len(result)):
            result[i] = list(result[i])
            result[i][2] = cur.execute(f'select degree from roasting_degrees '
                                       f'where id = {result[i][2]}').fetchone()[0]
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(7)
        self.titles = 'ID', 'Название сорта', 'Степень обжарки', \
                      'Молотый/В зёрнах', 'Описание вкуса', 'Цена', 'Объём упаковки'
        self.tableWidget.setHorizontalHeaderLabels(self.titles)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.tableWidget.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())