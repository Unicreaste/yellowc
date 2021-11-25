from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import sys
import random
from circles import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
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
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            qp.setBrush(QColor(r, g, b))
            r = random.randint(2, 50)
            qp.drawEllipse(50, 50, r, r)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())