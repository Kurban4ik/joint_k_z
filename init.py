import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QButtonGroup, QDialog


# Окно инициализации
class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('data/init.ui', self)
        self.gooo.clicked.connect(self.shutdown)
    # это функция которая отслыает параметры после выбора танков обоими игроками, вооружения и карты
    def shutdown(self):
        self.p1 = []  # игрок 1
        self.p2 = []  # игрок 2
        self.map = 1
        # выборка параметров из radioButton
        for i in self.buttonGroup.buttons():
            if i.isChecked():
                if i.text() == 'Тяжёлый танк':
                    self.p1.append(1)
                elif i.text() == 'Средний танк':
                    self.p1.append(2)
                else:
                    self.p1.append(3)

        for i in self.buttonGroup_2.buttons():
            if i.isChecked():
                if i.text() == 'Крупный снаряд':
                    self.p1.append(1)
                elif i.text() == 'Средний снаряд':
                    self.p1.append(2)
                else:
                    self.p1.append(3)
        # Выборка параметров для второго игрока
        for i in self.buttonGroup_3.buttons():
            if i.isChecked():
                if i.text() == 'Тяжёлый танк':
                    self.p2.append(1)
                elif i.text() == 'Средний танк':
                    self.p2.append(2)
                else:
                    self.p2.append(3)

        for i in self.buttonGroup_4.buttons():
            if i.isChecked():
                if i.text() == 'Крупный снаряд':
                    self.p2.append(1)
                elif i.text() == 'Средний снаряд':
                    self.p2.append(2)
                else:
                    self.p2.append(3)

        if self.map_2.isChecked():
            self.map = 2
        elif self.map_3.isChecked():
            self.map = 3
        elif self.map_4.isChecked():
            self.map = 4

        self.close()

# я собираюсь создавать класс mainwindow, а затем передавать через экземпляр вызываемого класса параметры

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.exec_()
    print(ex.map, ex.p1, ex.p2)
    if ex.map == 1:
        pass
