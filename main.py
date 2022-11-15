import random

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.repaint)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        r, g, b = random.randrange(256), random.randrange(256), random.randrange(256)
        qp.setBrush(QColor(r, g, b))
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
