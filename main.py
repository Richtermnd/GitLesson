import random

from PyQt5 import uic
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(r'UI.ui', self)
        self.pushButton.clicked.connect(self.repaint)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(*self.rand_circle())
        qp.end()

    def rand_circle(self):
        r = random.randrange(10, 100)
        center = QPoint(random.randrange(r, self.width() - r), random.randrange(r, self.height() - r))
        return center, r, r


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())