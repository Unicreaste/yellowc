from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
import sys
import random

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('UI.ui', self)
        self.draw = 0
        self.pushButton.clicked.connect(self.paint)


    def paint(self):
        self.draw = 1
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor('yellow'))
            r = random.randint(2, 50)
            qp.drawEllipse(50, 50, r, r)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())