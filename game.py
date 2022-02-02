import sys
print()

from PyQt5.QtWidgets import QApplication

from init import MainWindow
from map_1 import map_1
from map_2 import map_2
from map_3 import map_3
from map_4 import map_4

app = QApplication(sys.argv)
ex = MainWindow()
ex.exec_()

if ex.map == 1:
    map_1(*ex.p1, *ex.p2)
elif ex.map == 2:
    map_2(*ex.p1, *ex.p2)
elif ex.map == 3:
    map_3(*ex.p1, *ex.p2)
else:
    map_4(*ex.p1, *ex.p2)
