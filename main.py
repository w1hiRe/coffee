import sys
import sqlite3
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QTableWidgetItem


class Espresso(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.setWindowTitle('Эспрессо')
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM Espresso
                    WHERE id = 1""").fetchall()
        self.tableWidget.insertRow(0)
        for elem in result:
            self.tableWidget.setItem(0, 0, QTableWidgetItem(str(elem[1])))
            self.tableWidget.setItem(0, 1, QTableWidgetItem(str(elem[2])))
            self.tableWidget.setItem(0, 2, QTableWidgetItem(str(elem[3])))
            self.tableWidget.setItem(0, 3, QTableWidgetItem(str(elem[4])))
            self.tableWidget.setItem(0, 4, QTableWidgetItem(str(elem[5])))
            self.tableWidget.setItem(0, 5, QTableWidgetItem(str(elem[6])))
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Espresso()
    ex.show()
    sys.exit(app.exec())